Microservice Communication Contract

In order to properly run the microservice quiz properly the UI must be able to make a request to the program specifically looking for the 'quiz_microservice.txt' file
Within the quiz_microservice.txt file, the microservice will only run if there is a string of "run" within the text file.

Depending on the difficulty setting, the microservice will specify Beginner, Intermediate, or Advanced, depending on what the user has selected. Once the user goes through the quiz,
a score will be generated based off of the correct answers. The correct answers will then be generated again, and the UI can read these scores if the user selects the appropriate command line intervace (CLI) command to 
view the scores.

The quiz score will generate a text and also print out the score on the CLI.


