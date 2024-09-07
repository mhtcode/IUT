package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"errors"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/exporters/stdout/stdouttrace"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.4.0"
	"go.opentelemetry.io/otel/trace"
)

type book struct {
	ID       string `json:"id"`
	Title    string `json:"title"`
	Author   string `json:"author"`
	Quantity int    `json:"quantity"`
}

var books = []book{
	{ID: "1", Title: "Book 1", Author: "Author 1", Quantity: 10},
	{ID: "2", Title: "Book 2", Author: "Author 2", Quantity: 2},
	{ID: "3", Title: "Book 3", Author: "Author 3", Quantity: 1},
}

func getBooks(c *gin.Context) {
	tracer := otel.Tracer("example.com/trace")

	ctx, span := tracer.Start(c.Request.Context(), "getBooks")
	defer span.End()

	c.IndentedJSON(http.StatusOK, books)
	span.AddEvent("Fetched all books", trace.WithAttributes(attribute.Key("count").Int(len(books))))
}

func searchBooksById(ctx context.Context, id string) (*book, error) {
	tracer := otel.Tracer("example.com/trace")

	_, span := tracer.Start(ctx, "searchBooksById")
	defer span.End()

	for i, b := range books {
		if id == b.ID {
			span.SetAttributes(attribute.Key("book.id").String(id))
			return &books[i], nil
		}
	}
	return nil, errors.New("book not found")
}

func getBookById(c *gin.Context) {
	id := c.Param("id")
	tracer := otel.Tracer("example.com/trace")

	ctx, span := tracer.Start(c.Request.Context(), "getBookById")
	defer span.End()

	book, err := searchBooksById(ctx, id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found"})
		span.SetAttributes(attribute.Key("error").String(err.Error()))
		return
	}
	c.IndentedJSON(http.StatusOK, book)
}

func checkOutBook(c *gin.Context) {
	id, ok := c.GetQuery("id")
	if !ok {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Missing id query parameter"})
		return
	}
	tracer := otel.Tracer("example.com/trace")

	ctx, span := tracer.Start(c.Request.Context(), "checkOutBook")
	defer span.End()

	book, err := searchBooksById(ctx, id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found"})
		span.SetAttributes(attribute.Key("error").String(err.Error()))
		return
	}
	if book.Quantity <= 0 {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Book not available"})
		return
	}
	book.Quantity -= 1
	c.IndentedJSON(http.StatusOK, book)
}

func checkInBook(c *gin.Context) {
	id, ok := c.GetQuery("id")
	if !ok {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Missing id query parameter"})
		return
	}
	tracer := otel.Tracer("example.com/trace")

	ctx, span := tracer.Start(c.Request.Context(), "checkInBook")
	defer span.End()

	book, err := searchBooksById(ctx, id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found"})
		span.SetAttributes(attribute.Key("error").String(err.Error()))
		return
	}
	book.Quantity += 1
	c.IndentedJSON(http.StatusOK, book)
}

func addBook(c *gin.Context) {
	var newBook book
	err := c.BindJSON(&newBook)
	if err != nil {
		return
	}

	tracer := otel.Tracer("example.com/trace")
	var span trace.Span
	ctx, span = tracer.Start(c.Request.Context(), "addBook")
	defer span.End()

	for i, b := range books {
		if newBook.ID == b.ID {
			c.IndentedJSON(http.StatusBadRequest, gin.H{"message": fmt.Sprintf("Book already exists with id = %s", b.ID)})
			span.SetAttributes(attribute.Key("error").String(fmt.Sprintf("Book already exists with id = %s", b.ID)))
			return
		}
	}

	books = append(books, newBook)
	c.IndentedJSON(http.StatusCreated, newBook)
}

func main() {
	cleanup := InitTracer()
	defer cleanup()

	router := gin.Default()
	router.GET("/getBooks", getBooks)
	router.GET("/getBooks/:id", getBookById)
	router.POST("/addBook", addBook)
	router.PATCH("/checkOutBook", checkOutBook)
	router.PATCH("/checkInBook", checkInBook)
	router.Run("localhost:8080")
}
