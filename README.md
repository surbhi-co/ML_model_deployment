# Online_shopper's_intention_ML_model

 ## Problem statement 
 Given a dataset consisting of a no. of sessions of users along with certain attributes,We need to predict whether a session would end with shopping or not.

 ## Dataset Dictionary
 The data set consists of 12330 sessions, along with 18 attributes.
 Each session belongs to a different user in a 1-year period.
 
 ATTRIBUTES
## Administrative: *No. of adiministrative pages visted by the user in a session.*
## Administrative Duration : *Time spent on the administrative pages by the user in a session.*
## Informational : *No. of Informational pages visted by the user in a session.*
## Informational Duration : *Time spent on the Informational pages by the user in a session.*
## Product Related : *No. of Product Related pages visted by the user in a session.*
## Product Related Duration :*Time spent on the Product related pages by the user in a session.*
## Bounce Rate: *Refers to the percentage of visitors who enter the site from that page and then left without triggering any other requests during that session.
## Exit Rate :*The percentage of pageveiws that ended up on that page in a session.*
## Page Value :*This feature represents the average value for a web page that a user visited before completing an e-commerce transaction.*
## Special Day : *This feature indicates the closeness of the site visiting time to a specific special day in which the sessions are more likely to be finalized with transaction*
## operating system:*Integer value representing the operating system the user was using during teh session.*
## browser: *intger value depictimg the browser, user was on.*
## region :*integer representing the user's loaction.*
## traffic type :*integer representing what is the traffic type of the user.*
## visitor type : *category of user type, such as returning or new user.* 
## Weekend : *a Boolean value indicating whether the date of the visit is weekend*
## Month : *month of the year for the session.*

## NOTE: 
Some columns have been dropped due to the lack of information on the value they hold such as traffic type, browser, region, operating system do not specify what exactly the integers signify.

The code forms the part of the procedure to preprocess the data and predict the label which in this case is the *Revenue* column.

