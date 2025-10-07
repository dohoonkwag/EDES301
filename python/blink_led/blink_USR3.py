"""
--------------------------------------------------------------------------
USR3 LED Blink
--------------------------------------------------------------------------
License:   
Copyright 2025 - Dohoon Kwag

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple program that will 
  - Make the PocketBeagle's USR3 LED blink at 5Hz

Error conditions:
  - Keyboard Interrupt --> Program should exit

--------------------------------------------------------------------------
"""

# ------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------
import Adafruit_BBIO.GPIO as LED
import time

# ------------------------------------------------------------------------
# Main Script
# ------------------------------------------------------------------------
if __name__ == "__main__":
    # Create LED object for USR3
    usr3 = LED.LED("USR3")

    try:
        while True:
            usr3.on()
            time.sleep(0.1)   # LED ON for 0.1 seconds
            usr3.off()
            time.sleep(0.1)   # LED OFF for 0.1 seconds

    except KeyboardInterrupt:
        # Turn off LED before exiting
        usr3.off()
        print("\nExiting program.")