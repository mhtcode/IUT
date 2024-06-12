/*
 * Micro_HW02_40006133.c
 *
 * Created: 12/23/2023 8:19:17 PM
 * Author : masih tanoursaz
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>

int main(void)
{
	DDRB |= 0x20;
	
	TCNT0 = -32;
	TCCR0 = 0x01;
	
	TIMSK = (1<<TOIE0);
	
	sei();
	
	DDRC = 0x00;
	DDRD = 0xFF;
	
	while(1)
	PORTD = PINC;
}
ISR (TIMER0_OVF_vect)
{
	TCNT0 = -32;
	PORTB ^= 0x20;
}


