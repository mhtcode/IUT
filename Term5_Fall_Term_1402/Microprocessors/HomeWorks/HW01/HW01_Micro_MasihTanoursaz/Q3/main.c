/*
 * Micro_HW03_40006133.c
 *
 * Created: 12/23/2023 9:24:38 PM
 * Author : masih tanoursaz
 */ 

<<<<<<< HEAD
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#define F_CPU 8000000UL
#define TRUE 1

ISR(INT0_vect) {
		PORTC++;
}

ISR(INT1_vect) {
		PORTC--;
}

void createPulse() {
	PORTD ^= (1 << PD4);
}



int main() {
	PORTC = 0x00;
	DDRC = 0xFF;
	
	DDRD |= (1 << PD4);

	
	GICR |= (1 << INT0) | (1 << INT1);
	MCUCR |= (1 << ISC01) | (1 << ISC00) ; 
	MCUCR |= (1 << ISC11) | (1 << ISC10);
	sei(); 
	while (TRUE) {
		if (PORTC > 100 && PORTC < 200) {
			createPulse();
			 _delay_ms(500);
		}
	}

	return 0;
}




=======
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#define F_CPU 8000000UL
#define TRUE 1

ISR(INT0_vect) {
		PORTC++;
}

ISR(INT1_vect) {
		PORTC--;
}

void createPulse() {
	PORTD ^= (1 << PD4);
}



int main() {
	PORTC = 0x00;
	DDRC = 0xFF;
	
	DDRD |= (1 << PD4);

	
	GICR |= (1 << INT0) | (1 << INT1);
	MCUCR |= (1 << ISC01) | (1 << ISC00) ; 
	MCUCR |= (1 << ISC11) | (1 << ISC10);
	sei(); 
	while (TRUE) {
		if (PORTC > 100 && PORTC < 200) {
			createPulse();
			 _delay_ms(500);
		}
	}

	return 0;
}




>>>>>>> 10f5617 (Term 5 Completed)

