from queue import Queue
#import time
import requests

api_base_url = 'https://dummyjson.com/products/1'

class JobManager:
    def __init__(self, jobs, queue_framework):
        self.jobs = jobs if jobs is not None else []
        self.queue_framework = queue_framework if queue_framework is not None else api_base_url

    def access_queue(self):
        try:
            response = requests.get(f"{self.queue_framework}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error accessing queue: {e}")
            return None
        
    def is_empty(self, queue_framework):
        """Check if the queue is empty."""
        if self.jobs is not (None or []) or queue_framework is not (None or []):
            return  self.jobs == [], queue_framework == []

    def allJobs(self):
        try:
            response = requests.get(f"{self.queue_framework}") #/all_jobs")
            response.raise_for_status()
            return self.jobs, response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting all jobs: {e}")
            return None

    def currentProcessingJobs(self):
        try:
            response = requests.get(f"{self.queue_framework}") #/current_processing_jobs")
            response.raise_for_status()
            currentProcessingJobs = [job for job in self.jobs if job["status"] == "InProgress"]
            return currentProcessingJobs, response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting current processing jobs: {e}")
            return None

    def updateJobStatus(self, id, new_status):
        try:
            response = requests.get(f"{self.queue_framework}") #/update_job_status/{id}/{new_status}
            response.raise_for_status()
            for job in self.jobs:
             if job["id"] == id:
                job["status"] = new_status
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating job status: {e}")
            return None

    def nextRunJobs(self):
        try:
            response = requests.get(f"{self.queue_framework}") #/next_run_jobs")
            response.raise_for_status()
            new_jobs = [job for job in self.jobs if job["status"] == "new"]
            return new_jobs, response.json() 
        except requests.exceptions.RequestException as e:
            print(f"Error getting next run jobs: {e}")
            return None


if __name__ == "__main__":

    jobs = [
    {"id": 1, "type": "Job1", "status": "completed"},
    {"id": 2, "type": "Job2", "status": "InProgress"},
    {"id": 3, "type": "Job3", "status": "new"},
    ]

    job_manager = JobManager(jobs, queue_framework=None)

    # Access the queue from the module
    accessed_queue = job_manager.access_queue()
    print("Accessed Queue:", accessed_queue)

    # Get all jobs
    all_jobs = job_manager.allJobs()
    print("All Jobs:", all_jobs)

    # Get current processing jobs
    current_processing_jobs = job_manager.currentProcessingJobs()
    print("Current Processing Jobs:", current_processing_jobs)

    # Get updated jobs
    new_status = "Completed"
    update_job_status = job_manager.updateJobStatus(1, new_status)
    print("Updated Jobs:", update_job_status)

    # Get next run job
    next_run_job = job_manager.nextRunJobs()
    print("Next Run Job:", next_run_job)

