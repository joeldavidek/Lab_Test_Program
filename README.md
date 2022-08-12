# Lab_Test_Program

 This program is coded all in Python using the tkinter module. 

I created this program as a way to record test data in a simple way. I based it off of what I do at work. We currently use a notebook to record data and I thought that this could be helpful. What I do for work is produce different grades of emulsion. For example, the button the says "CSS-1H" is one grade of emulsion. In simplified terms, emulsion is a blend of crude oil and water. Everything that is entered in on the left side of the program is then added to the "Results" section after the user presses enter. After all of the data is entered and the user selects the "Submit" button, the data is then transfered to a text file that is organized and easy to read. I chose a simple text file because once you have lots of data, its easy enough to do a "ctrl f" or control find to find what you're looking for. 

Let me explain what the prompts are and how they work: 

Batch#: In most physical production environments products are done in batches. for example, if you were brewing beer, you would do it in batches. This entry is where you'd input what batch number you're on. Input a number or code and press enter on your keyboard. It will now show up in the results section. There is a status indicator on the bottom right hand corner that says "Ready", once you enter in a batch number it will change to that number as well.

Product: This is the section where you'd select what product you are testing. Click the button and it will show up in the results section.

Tank: This is where you'd enter what tank the sample you took to test came out of. Enter in a tank number or code, and press enter on your keyboard.

Sieve: In emulsion testing, there is a test called a sieve test. This is where you take your sample and poor it through a screen, kind of like a sift. It catches any solidified chunks. If there are too many chunks, the test failed, if the screen is clear with little to no chunks, the test passed. Press the "Pass" or "Fail" button and it will show up in the results section.

Residue 1 and Residue 2: A residue test is where you take a small amount of your sample and poor it into a container. The amount is usually measured in ounces. That small amount is then heated to evaporate any water that is in the sample. Whats left is your residue. the first entry is the weight of the sample before you heat it. The second entry is the weight after you've heated it and all of the water has evaporated. 

Final Residue: The final residue is the calculation you do to find out what percentage of your product is crude oil. The calulate button does this for you. It takes Residue 2 and divides it by Residue 1. It then multiplies it by 100 and rounds the number to the nearest hundreth.

Viscosity: A viscosity test is where you find out how thick your product is, or how fast it drips. This is measured in seconds. Enter in your result in seconds and press enter. It will show up in the results section along with the result converted into minutes and seconds, like what you would see on a stopwatch.

Comments: This is where you can enter in any addtional notes or comments.

Submit: This button sends the results over to a text file called "Test_Results.txt". It will create the file for you and appened the results. Every test after your first one will submit to the same file.


Thanks for reading. If anyone is iterested in this program, I can modify it to suit the kind of tests you need.
