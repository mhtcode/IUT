//*
//* Micro_40006133_HW02_SenderSyn.c
//*
//* Created: 12/28/2023 8:16:35 PM
//* Author : masih tanoursaz
//*
<<<<<<< HEAD
#define F_CPU 8000000UL			/* Define frequency here its 8MHz */
#include <avr/io.h>
#include <util/delay.h>

#define USART_BAUDRATE 9600
#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)


void usart_init()
{
	UCSRB |= (1 << RXEN) | (1 << TXEN);/* Turn on transmission and reception */
	UCSRC |= (1 << URSEL) | (1 << UCSZ0) | (1 << UCSZ1);/* Use 8-bit character sizes */
	UBRRL = BAUD_PRESCALE;		/* Load lower 8-bits of the baud rate value */
	UBRRH = (BAUD_PRESCALE >> 8);	/* Load upper 8-bits*/
}

unsigned char usart_reciever()
{
	while ((UCSRA & (1 << RXC)) == 0);/* Wait till data is received */
	return(UDR);			/* Return the byte*/
}

void usart_transmitter(char ch)
{
	while (! (UCSRA & (1<<UDRE)));	/* Wait for empty transmit buffer*/
	UDR = ch ;
}

void usart_SendString(char *str)
{
	unsigned char j=0;
	
	while (str[j]!=0)		/* Send string till null */
	{
		usart_transmitter(str[j]);
		j++;
	}
}

int main()
{
	char c;
	usart_init();
	usart_SendString("sr");
	while(1)
	{
		c=usart_reciever();
		_delay_ms(1000);
		usart_transmitter(c);
	}
=======
#define F_CPU 8000000UL			/* Define frequency here its 8MHz */
#include <avr/io.h>
#include <util/delay.h>

#define USART_BAUDRATE 9600
#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)


void usart_init()
{
	UCSRB |= (1 << RXEN) | (1 << TXEN);/* Turn on transmission and reception */
	UCSRC |= (1 << URSEL) | (1 << UCSZ0) | (1 << UCSZ1);/* Use 8-bit character sizes */
	UBRRL = BAUD_PRESCALE;		/* Load lower 8-bits of the baud rate value */
	UBRRH = (BAUD_PRESCALE >> 8);	/* Load upper 8-bits*/
}

unsigned char usart_reciever()
{
	while ((UCSRA & (1 << RXC)) == 0);/* Wait till data is received */
	return(UDR);			/* Return the byte*/
}

void usart_transmitter(char ch)
{
	while (! (UCSRA & (1<<UDRE)));	/* Wait for empty transmit buffer*/
	UDR = ch ;
}

void usart_SendString(char *str)
{
	unsigned char j=0;
	
	while (str[j]!=0)		/* Send string till null */
	{
		usart_transmitter(str[j]);
		j++;
	}
}

int main()
{
	char c;
	usart_init();
	usart_SendString("sr");
	while(1)
	{
		c=usart_reciever();
		_delay_ms(1000);
		usart_transmitter(c);
	}
>>>>>>> 10f5617 (Term 5 Completed)
}