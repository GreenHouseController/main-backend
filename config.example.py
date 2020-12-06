# Used to mock the connection to the raspberry pi
# This helps us develop the application locally without being connected to a raspberry pi
mock_pi = True

# Used to control our flask webserver
flask = {
    "debug": True, # Print extra debug lines useful for troubleshooting
    "port": 8000   # Which port the server should listen to for requests
}