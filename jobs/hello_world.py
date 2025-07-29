from nautobot.apps.jobs import Job, register_jobs, StringVar

name = "Hello World Nautobot Jobs"

class HelloJobs(Job):

    class Meta:
        name = "Hello Jobs"
        description = "Hello World for first Nautobot Jobs"

    def run(self):
        self.logger.debug("Hello, this is my first Nautobot Job.")

class HelloJobsWithLogs(Job):

    class Meta:
        name = "Hello Jobs with Logs"
        description = "Hello Jobs with different log types"

    def run(self):
        self.logger.info("This is an info type log.")
        self.logger.debug("This is a debug type log.")
        self.logger.warning("This is a warning type log.")
        self.logger.error("This is an error type log.")
        self.logger.critical("This is a critical type log.")
class HelloJobsWithInputs(Job):
    
    username = StringVar()

    class Meta:
        name = "Hello Jobs with User Inputs"
        description = "Hello Jobs with Different User Inputs"

    def run(self, username):
        self.logger.info(f"Hello Jobs with {username}.")


register_jobs(
    HelloJobs,
    HelloJobsWithLogs,
    HelloJobsWithInputs,
)