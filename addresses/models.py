from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPES=(
	('billing','Billing'),
	('shipping','Shipping'),
)
# Create your models here.
class Address(models.Model):
	billing_profile=models.ForeignKey(BillingProfile)
	address_type=models.CharField(max_length=120,choices=ADDRESS_TYPES)
	address_line_1=models.CharField(max_length=120)
	address_line_2=models.CharField(max_length=120,null=True,blank=True)
	city=models.CharField(max_length=120)
	country=models.CharField(max_length=120,default='United States of America')
	state=models.CharField(max_length=120)
	postal_code=models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)
	def get_address(self):
		return "{line1}\n{line2}\n{city}\n{state}\n{country}\n{postal_code}".format(
				line1=self.address_line_1,
				line2=self.address_line_2,
				city=self.city,
				state=self.state,
				country=self.country,
				postal_code=self.postal_code,
			)