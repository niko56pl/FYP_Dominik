from django.db import models

YEARS = (  
    ('', ''),
    ('2020', '2020'),
	('2019', '2019'),
	('2018', '2018'),
	('2017', '2017'),
	('2016', '2016'),
	('2015', '2015'),
	('2014', '2014'),
	('2013', '2013'),
	('2012', '2012'),
	('2011', '2011'),
	('2010', '2010'),
	('2009', '2009'),
	('2008', '2008'),
	('2007', '2007'),
	('2006', '2006'),
	('2005', '2005'),
	('2004', '2004'),
	('2003', '2003'),
	('2002', '2002'),
	('2001', '2001'),
	('2000', '2000'),
	('1999', '1999'),
	('1998', '1998'),
	('1997', '1997'),
	('1996', '1996'),
	('1995', '1995'),
	('1994', '1994'),
	('1993', '1993'),
	('1992', '1992'),
	('1991', '1991'),
	('1990', '1990'),
	('1989', '1989'),
	('1988', '1988'),
	('1987', '1987'),
)
MAKES = (  
    ('', ''),
	#('ABARTH', 'Abarth'),
    ('FORD', 'Ford'),
    ('AUDI', 'Audi'),
)
MODELS = (  
    ('', ''),
	#('500', '500'),
	#('595', '595'),
    ('CMAX', 'C-Max'),
    ('FOCUS', 'Focus'),
    ('A3', 'A3'),
    ('A4', 'A4'),
)
LITERS = (  
    ('', ''),
    ('0.6', '0.6'),
	('0.7', '0.7'),
	('0.8', '0.8'),
	('0.9', '0.9'),
	('1.0', '1.0'),
    ('1.1', '1.1'),
    ('1.2', '1.2'),
    ('1.3', '1.3'),
    ('1.4', '1.4'),
    ('1.5', '1.5'),
    ('1.6', '1.6'),
    ('1.7', '1.7'),
    ('1.8', '1.8'),
    ('1.9', '1.9'),
    ('2.0', '2.0'),
    ('2.1', '2.1'),
    ('2.2', '2.2'),
    ('2.3', '2.3'),
    ('2.4', '2.4'),
    ('2.5', '2.5'),
    ('2.6', '2.6'),
    ('2.7', '2.7'),
    ('2.8', '2.8'),
    ('2.9', '2.9'),
    ('3.0', '3.0'),
    ('3.2', '3.2'),
    ('3.5', '3.5'),
    ('3.7', '3.7'),
    ('3.8', '3.8'),
    ('4.0', '4.0'),
    ('4.2', '4.2'),
    ('4.4', '4.4'),
    ('4.5', '4.5'),
    ('4.6', '4.6'),
    ('4.9', '4.9'),
    ('5.0', '5.0'),
    ('5.2', '5.2'),
    ('5.4', '5.4'),
    ('5.5', '5.5'),
    ('5.6', '5.6'),
    ('5.7', '5.7'),
    ('5.8', '5.8'),
    ('6.0', '6.0'),
    ('6.2', '6.2'),
    ('6.5', '6.5'),
    ('6.7', '6.7'),
    ('6.9', '6.9'),
    ('7.0', '7.0'),
    ('7.4', '7.4'),
    ('8.0', '8.0'),
    ('8.4', '8.4'),
)

FUELS =  (
	('', ''),
	('Petrol', 'Petrol'),
	('Diesel', 'Diesel'),
	('Hybrid', 'Hybrid'),
)

MILEAGES =  (
	('', ''),
	('1500', '1500'),
	('0-10000', '0 - 10,000km'),
	('10000-50000', '10,000 - 50,000km'),
	('50000-100000', '50,000 - 100,000km'),
	('100000-150000', '100,000 - 150,000km'),
	('150000-200000', '150,000 - 200,000km'),
	('200000-250000', '200,000 - 250,000km'),
	('250000-300000', '250,000 - 300,000km'),
	('300000-350000', '300,000 - 350,000km'),
	('>350000', '350,000+ km'),
)

DATES = (  
    ('Mar2020', 'March 2020'),
	('Apr2020', 'April 2020'),
	('May2020', 'May 2020'),
)

class Query(models.Model):  
	MAKE    = models.CharField(max_length = 50, choices=MAKES)
	MODEL   = models.CharField(max_length = 50, choices=MODELS)
	YEAR    = models.IntegerField(max_length = 4, choices=YEARS)
	LITER   = models.CharField(max_length = 3, choices=LITERS)
	FUEL    = models.CharField(max_length = 6, choices=FUELS)
	#MILEAGE = models.IntegerField(max_length = 13, choices=MILEAGES)
	#ENTERED = models.DateField(max_length = 20, choices=DATES)
	
class Average(models.Model):
	#price = models.ForeignKey(Price, on_delete=models.CASCADE)
	class Meta:
		db_table = 'ford_cmax'
	
	make	= models.CharField(max_length = 15)
	model	= models.CharField(max_length = 20)
	year    = models.IntegerField(max_length = 4)
	liter   = models.CharField(max_length = 3)
	fuel    = models.CharField(max_length = 6)
	price = models.IntegerField(max_length = 6)
	entered = models.DateTimeField(primary_key=True)
	
	#mileage = models.IntegerField(max_length = 10)
	
	def __str__(self):
		return self.title
# Makes data in table more visible
