# Nautobot Database Model Part 3: Data Integrity and Security

Data integrity and security are two areas we will focus on for today's challenge.

We want to make sure data in our databases remain accurate, consistent, and reliable. In Nautobot, we can do this by enforcing the fields with constraints, validation, and certain relationships between models.

Security in Nautobot involves protecting data from unauthorized access, ensuring data confidentiality, integrity, and availability.

## Environment Setup

We will use a combination of [Scenario 2](../Lab_Setup/scenario_2_setup/README.md) lab, [https://demo.nautobot.com/](https://demo.nautobot.com/), and [Nautobot Documentation](https://docs.nautobot.com/projects/core/en/latest/user-guide/core-data-model/overview/introduction/) for today's challenge. 

## Data Integrity 

We have already seen many of the concepts applied in the data model creation, let's review them: 

**Field Constraints**: Define constraints on individual fields to ensure they store valid data. Examples include setting *max_length* for *CharField*, *unique=True* for fields that must have unique values, and *null=True* for fields that can be empty.

**Model Validation**: Implement custom validation methods within your models to enforce complex validation rules that can't be captured by field constraints alone.

**Database Relationships**: Use relationships such as *ForeignKey*, *OneToOneField*, and *ManyToManyField* to maintain referential integrity between models. The *on_delete* parameter in *ForeignKey* ensures that related data is handled appropriately when a referenced object is deleted.

Looking back at [Day 62](../Day062_Database_Models_2_Custom_Models/README.md) custom models, we created the following code related to the data integrity concepts: 

```
class Asset(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    warranty_expiration = models.DateField()

    def __str__(self):
        return f"Asset {self.serial_number} for {self.device}"
```

## Security 

Security in Nautobot involves protecting data from unauthorized access. Key security practices include:

- **Authentication and Authorization**: Use Django's built-in authentication system to manage user access. Define user roles and permissions to control who can view or modify data.

- **Field-Level Security**: Use Nautobot's [object permissions](https://docs.nautobot.com/projects/core/en/stable/user-guide/platform-functionality/users/objectpermission/) to restrict access to sensitive fields.

- **Audit Logging**: Enable audit logging to track changes made to data. This helps in monitoring and detecting unauthorized changes.

It is also worth pointing out that many of the security settings are set in `nautobot_config.py`, although we relaxed some of them in the development environment: 

![nautobot_config_settings](images/nautobot_config_settings.png)

Congratulations on completing Day 63! 

## Day 63 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). 

Go ahead and post your thought on data integrity and security in Nautobot from today's challenge on a social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will discuss database migration. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+60+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 60 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot-challenge, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 