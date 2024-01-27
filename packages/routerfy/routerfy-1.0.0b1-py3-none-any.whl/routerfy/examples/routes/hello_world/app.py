from route import router

def lambda_handler(event):
    return router.handle_request(event)