import pandas as pd
from django.db import models

class PredictionModel:
    @staticmethod
    def predict(name, yor, NA, EU, JP, score, critic_count, user_count, console, dev, rate, pub):
        if name == "":
            return 0

        # Convert input values
        console = console_func(console)
        dev = dev_func(dev)
        pg_rate = rate_func(rate)
        pub = pub_func(pub)

        df2 = {
            'Year_of_Release': int(yor), 'NA_Sales': float(NA), 'EU_Sales': float(EU),
            'JP_Sales': float(JP), 'Critic_Score': float(score), 'Critic_Count': float(critic_count),
            'User_Count': int(user_count), 'PC': console[0], 'PS2': console[1], 'PS3': console[2],
            'X360': console[3], 'other_console': console[4], 'Capcom': dev[0], 'EA': dev[1],
            'Komani': dev[2], 'Ubisoft': dev[3], 'other_dev': dev[4], 'E': pg_rate[0], 'E10+': pg_rate[1],
            'M': pg_rate[2], 'T': pg_rate[3], 'other_rating': pg_rate[4], 'Activision': pub[0],
            'Electronic Arts': pub[1], 'Konami Digital Entertainment': pub[2], 'Nintendo': pub[3],
            'Sony Computer Entertainment': pub[4], 'Ubisoft': pub[5], 'other_publisher': pub[6]
        }

        # Placeholder prediction logic (replace this with actual computation)
        res = df2['Critic_Score'] * 0.1 + df2['User_Count'] * 0.05  # Example: Some random logic
        return round(abs(res), 2)

def console_func(x):
    options = ['PC', 'PS2', 'PS3', 'X360']
    return [1 if x == option else 0 for option in options] + [1 if x not in options else 0]

def dev_func(x):
    options = ['Capcom', 'EA', 'Komani', 'Ubisoft']
    return [1 if x == option else 0 for option in options] + [1 if x not in options else 0]

def rate_func(x):
    options = ['E', 'E10+', 'M', 'T']
    return [1 if x == option else 0 for option in options] + [1 if x not in options else 0]

def pub_func(x):
    options = ['Activision', 'Electronic Arts', 'Konami Digital Entertainment', 'Nintendo',
               'Sony Computer Entertainment', 'Ubisoft']
    return [1 if x == option else 0 for option in options] + [1 if x not in options else 0]


from django.db import models

class GameData(models.Model):
    name = models.CharField(max_length=255)
    year_of_release = models.IntegerField()
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    critic_score = models.FloatField()
    critic_count = models.IntegerField()
    user_count = models.IntegerField()
    console = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    rating = models.CharField(max_length=20)
    publisher = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    year_of_release = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    na_sales = models.FloatField(null=True, blank=True)
    eu_sales = models.FloatField(null=True, blank=True)
    jp_sales = models.FloatField(null=True, blank=True)
    other_sales = models.FloatField(null=True, blank=True)
    global_sales = models.FloatField(null=True, blank=True)
    critic_score = models.FloatField(null=True, blank=True)
    critic_count = models.IntegerField(null=True, blank=True)
    user_score = models.FloatField(null=True, blank=True)
    user_count = models.IntegerField(null=True, blank=True)
    developer = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


