from django.db import models


class Candidate(models.Model):
    """
    help: this class models a candidate contesting in an election.
    """
    name = models.CharField(max_length=30)
    Class = models.IntegerField()
    section = models.CharField(max_length=1) 
    votes = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, default="Female")
    image = models.ImageField(upload_to="static/voting")
    logo = models.ImageField(upload_to="static/voting",default=None)


    def __str__(self):
        return f"{self.name} from class {self.Class}-{self.section} is a candidate"
    
    def is_valid_candidate(self):
        if self.name != "" and 5 < self.Class <= 12:
            return True
        return False
    
    
    

    