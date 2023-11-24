# weatherapi
Building a Backend API for Weather Forecast using Python as the Programming language and Flask as the framework and theting the api with postman
# For execution of script follow these steps
#step1                                                                                                                                                                                                                 
run this script in the vs code make sure you have installed python on your device and also make sure the required libraries are installed like flask,requests                                                           
#step2                                                                                                                                                                                                                  
after hitting the run button in the terminal you will see the base url like http://127.0.0.1:5000 just open this in your browser.                                                                                       
by default this link is selected when you open this link you will see 404 error to fetch the weather you have to append this base url
with api endpoint  
/weather?location=city name #replace the city name with the name of the city of which you have to get the weather data                                                                                                 
add this above url with city name to base url and then you will get the weather data
ex:-http://127.0.0.1:5000/weather?location=bengaluru                                                                                                                                                                   
Thats it now you can see the json file NOTE:-make sure your script is running parallely in vs code 
![Screenshot (20)](https://github.com/sumeetpatil01/weatherapi/assets/136491586/5cbc83ee-f644-4ae2-809f-2d84f2a9d3a3)
# few screenshots to execute this
First pic shows to open the base url displayed in the terminal after running the script in vs code
![Screenshot (22)](https://github.com/sumeetpatil01/weatherapi/assets/136491586/c830eeb3-d1d7-4120-a799-daadeb7c8589)                                                                                                  

Second pic showing adding api endpoint to get the data after opening base url in browser 
![Screenshot (23)](https://github.com/sumeetpatil01/weatherapi/assets/136491586/f11e6ccc-0677-4edb-b8d3-00a51d8b2bc2)

Output
![Screenshot (24)](https://github.com/sumeetpatil01/weatherapi/assets/136491586/f487be43-6a8f-494f-8d02-73ad9cdcfe72)
after following all the steps you will get the result in json file you can also change the city name and try with other locations                                                                                  
after getting the output copy that url in your browser and test the api with postman






