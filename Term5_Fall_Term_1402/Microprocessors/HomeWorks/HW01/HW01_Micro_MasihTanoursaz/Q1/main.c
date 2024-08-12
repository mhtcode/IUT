/*
 * Micro_HW01_40006133.c
 *
 * Created: 12/23/2023 7:02:35 PM
 * Author : masih tanoursaz
 */ 

#include <avr/io.h>


int main(void)
{
    PORTB = 0x01;
	DDRC = 0xff;
	DDRD = 0xff;
	TCCR1A = 0x00;
	TCCR1B = 0x07;
	TCNT1L = 0x00;
	TCNT1H = 0x00;

    while (1) 
    {
		do 
		{
			PORTC = TCNT1L;
			PORTD = TCNT1H;
		} while ((TIFR&(0x1<<TOV1)) == 0);
		TIFR = 0x1<<TOV1;
    }
}

