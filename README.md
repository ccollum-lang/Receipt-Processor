# Receipt Processor
This is a docker file that runs a web application that receives and processes receipts. It has two main functions: storing receipts and calculating points for receipts. When a receipt is submitted, it is given a unique ID and stored in the application. When the points for a receipt are requested, the application retrieves the receipt data based on the provided ID and calculates the points using a set of rules. The points are then returned as a response. The application also uses various utility functions and modules for tasks such as generating unique IDs, parsing and manipulating dates and times, and handling HTTP requests and responses.

## Build the Image

To build the image, use the following command:
`docker build -t python-docker .`

## Running the Container

Create a container from the image using:
`docker run -d -p 8000:5000 python-docker`

