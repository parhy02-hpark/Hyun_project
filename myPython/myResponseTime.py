# Perform a basic performance test on REST API endpoint
import requests
import time

def performance(url, num_requests):
  response_time_list = []
  for i in range(num_requests):
    start_time = time.time()
    response = requests.get(url)  # <==  requests and get url
    end_time = time.time()
    # measure and report the response time for each request
    response_time = end_time - start_time
    response_time_list.append(response_time)
    print(f"response time: {response_time}")
    print(f"response time list: {response_time_list}")
  avg_response_time = sum(response_time_list) / len(response_time_list)
  print(f"average response time: {avg_response_time}")
 
if __name__ == "__main__":
  # send multiple requests to the endpoint
  api_url = "https://google.com"
  number_of_requests = 20
  performance(api_url, number_of_requests)
