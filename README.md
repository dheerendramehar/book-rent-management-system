# book-rent-management-system

**Code Exercise**  
Following is a programming exercise that we expect you to solve and come up with a solution. Tests
are mandatory.  

**Problem Statement**  
It is a program to calculate and print a statement of a customer's charges at a book rental store.
It is divided into 3 stories. Pick each story in sequence, solve it, test it, and then pick up next. Next
story should be applied in same solution and your design should start evolving.  
(**Note** - You need to create just one solution only which would satisfy all 3 stories)  

**Story 1**:
Customers can rent the books from the store. The rent changes will be calculated on the basis of
number of books rented and durations for each book it was rented. Per day rental charge is Rs 1.  
**Story 2**:
There are three kinds of books: regular, fiction, and novels. For Regular books renting per day charge
is Rs. 1.5. For fiction book renting per day charge is Rs. 3. For novels the per day charge is Rs. 1.5.  
**Story 3**:
The store decided to alter the calculations for Regular books and novels. Now for Regular books for
first 2 days charges will be Rs 1 per day and 1.5 Rs there after. Minimum charges will be considered
as Rs 2 if days rented is less than 2 days. Similarly for Novel minimum charges are introduced as 4.5
Rs if days rented is less than 3 days.  

**We'd like to see how your solution evolves with every new story. So, please implement the
stories in the given order, with at least one commit per story (of course, you may create as
many intermediate commits as you like). You may share your solution either as a zip file
(including the commits) or through github.**

Your solutions would be reviewed for:
1. Tests
2. Design of code
3. Domain models
4. Clean Code
5. Completeness of solution
Language - Any of your choice, but we would prefer a mainstream language like Python, Ruby, Java
or Javascript.  

**Additional Requirement**:
1. Dockerise the solution, host on a server and share the online link with us.
2. Describe the deployment steps with CI tool of your preference.


## Commands and links:
docker rm $(docker ps -a -q) # Remove all stopped containers  
xhost + # Allow clients to connect from any host to access the running X server  
docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <docker-image-id/name>

http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/  
https://superuser.com/a/392263/979451
