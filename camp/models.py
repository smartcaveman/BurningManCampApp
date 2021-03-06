from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser

undetermined = "dunno"
sharing_someone_elses = "sharing"
bringing_own_tent = "bringing"
sleep_in_vehicle = "car"
using_camp_yurt = "yurt"
other = "other"

Sleeping_arrangements = (
    (undetermined, "Not sure yet"),
    (bringing_own_tent, "Bringing own tent"),
    (sleep_in_vehicle, "Sleeping in own vehicle"),
    (using_camp_yurt, "Using camp yurt"),
    (sharing_someone_elses, "Sharing someone else's" ),
    (other, "Other"),
)

UNDETERMINED = 0
DRIVING = 1
RIDING_WITH = 2
OTHER = 3

Transit_arrangements = (
    (UNDETERMINED, "Not sure yet"),
    (DRIVING, "Primary driver"),
    (RIDING_WITH, "Riding with someone else"),
    (OTHER, "Some other transit")
)

PYB_days = (
    (0, "Monday"), # python day ints
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday")
)

Fish = "Fish"
Mammal = "Mammal"
Vegetarian = "Vegetarian"
Omnivore = "Omnivore"
Onions = "Onions"
Cucumber = "Cucumber"
Peppers = "Peppers"
Gluten_free = "Gluten_free"
Vegan = "Vegan"
Shellfish = "Shellfish"
Olives = "Olives"
Pork = "Pork"
Soy = "Soy"
Dairy = "Dairy"
Cilantro = "Cilantro"
Quinoa = "Quinoa"
Nightshades = "Nightshades"
Nuts = "Nuts"
Pescaterian = "Pescaterian"

What_are_you = (
    (Vegetarian, "Vegetarian"),
    (Vegan, "Vegan"),
    (Omnivore, "Omnivore"),
    (Pescaterian, "Pescaterian"),
    (Gluten_free, "Gluten_free")
)

Breakfast = "Breakfast"
Dinner = "Dinner"
Meals = (
    (Breakfast, "Breakfast"),
    (Dinner, "Dinner"),
    )

Chef = "Chef"
Sous_Chef = "Sous-Chef"
KP ="KP"
Shifts = (
    (Chef, "Chef"),
    (Sous_Chef, "Sous_Chef"),
    (KP, "KP"),
    )

Morning = "Morning"
Afternoon = "Afternoon"
PYB_shifts = (
    (Morning, "Morning"),
    (Afternoon, "Afternoon")
    )

nothing = "nothing"
needs_wheel_or_hub = "needs_wheel_or_hub"
tube = "tube"
brake_adjustment = "brake adjustment"
seat = "seat"
pedal = "pedal"
tire = "tire"
new_chain = "new_chain"
derailer = "derailer"
brake_repair = "brake repair"
head_tightening = "head tightening"
cable_repair_or_lube = "cable repair or lube"
other = "other"

Bike_repairs = (
    (nothing, "nothing"),
    (needs_wheel_or_hub, "needs_wheel_or_hub"),
    (tube, "tube"),
    (brake_adjustment, "brake adjustment"),
    (seat, "seat"),
    (pedal, "pedal"),
    (tire, "tire"),
    (new_chain, "new_chain"),
    (derailer, "derailer"),
    (brake_repair, "brake repair"),
    (head_tightening, "head tightening"),
    (cable_repair_or_lube, "cable repair or lube"),
    (other, "other")
    )


class Event(models.Model):
    name = models.CharField(max_length=500, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    @property
    def days(self):
        day = self.start_date
        while day < self.end_date:
            yield day
            day += timedelta(days=1)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('start_date',)

class MealRestriction(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class User(AbstractUser):
    # FIXME: if we don't want these nullable, we should have them as part of
    # signup.
    # FIXME: if we want to track attendance, we should pull out year-specific
    #  stuff to a separate model.
    playa_name = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    city = models.CharField(max_length=20, blank=True)
    cell_number = models.CharField(max_length=15, blank=True)
    emergency_contact_name = models.CharField(max_length=40, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)
    other_restrictions = models.CharField(max_length=100, blank=True)
    arrival_date =  models.DateTimeField(null=True, blank=True)
    departure_date = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    has_ticket = models.BooleanField(default=False)
    looking_for_ticket = models.BooleanField(default=True)
    camping_this_year = models.BooleanField(default=False)
    public_notes = models.TextField(blank=True, help_text="Tell us stuff that doesn't fit elsewhere.")

    meal_restrictions = models.ManyToManyField(MealRestriction, related_name="campers", blank=True)

    @property
    def display_name(self):
        return self.playa_name or \
            "%s %s" % (self.first_name, self.last_name) or \
            self.username

    def __unicode__(self):
        return '%s' % self.display_name

class Meal(models.Model):
    Breakfast = "Breakfast"
    Dinner = "Dinner"

    Kinds = (
         (Breakfast, "Breakfast"),
         (Dinner, "Dinner"),
    )

    event = models.ForeignKey(Event, help_text="What year/regional is this for?")
    day = models.DateField()
    kind = models.CharField(choices=Kinds, default=Dinner, max_length=10)
    chef = models.ForeignKey(User, null=True)
    private_notes = models.TextField(blank=True,
        help_text="Private to you")
    public_notes = models.TextField(blank=True,
        help_text="Public description")

    class Meta:
        ordering = ('day', 'kind')

    def __unicode__(self):
        return "%s %s %s" % (self.event, self.day, self.kind)

class MealShiftManager(models.Manager):
    def non_chef(self):
        return self.exclude(role=MealShift.Chef)

class MealShift(models.Model):
    Chef = "chef"
    Sous_Chef = "sous-chef"
    KP ="kp"
    Courier = "courier"

    Roles = (
        (Courier, "Courier"),
        (Chef, "Chef"),
        (Sous_Chef, "Sous Chef"),
        (KP, "KP"),
    )

    meal = models.ForeignKey(Meal, related_name='shifts')
    role = models.CharField(max_length = 10, choices=Roles, default=KP)
    worker = models.ForeignKey(User, null=True)

    objects = MealShiftManager()

    class Meta:
        ordering = ('meal', 'role', 'pk')

    def __unicode__(self):
        return "%s %s" % (self.meal, self.role)


def half_feet(start, stop):
    return [(i/12.0, i/12.0) for i in range(start * 12, stop * 12, 6)]

SIZE_CHOICES = half_feet(3, 20)

class Shelter(models.Model):
    user = models.OneToOneField(User)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    sleeping_arrangement = models.CharField(max_length=25, choices=Sleeping_arrangements)
    shelter_provider = models.ForeignKey(User, blank=True, null=True, related_name='provided_shelter')

    number_of_people_tent_sleeps = models.IntegerField(blank=True, default=0)
    sleeping_under_ubertent = models.BooleanField(default=False)
    width = models.FloatField(choices=SIZE_CHOICES, blank=True, null=True)
    length = models.FloatField(choices=SIZE_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return '%s in %s' % (self.user, self.sleeping_arrangement)

GIANT_SIZE_CHOICES = SIZE_CHOICES + half_feet(20, 99)

class Vehicle(models.Model):
    user = models.OneToOneField(User)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    transit_arrangement = models.IntegerField(choices=Transit_arrangements)
    transit_provider = models.ForeignKey(User, blank=True, null=True, related_name='provided_transit')

    model_of_car = models.CharField(max_length=25, blank=True, default='')
    make_of_car = models.CharField(max_length=15, blank=True, default='')
    width = models.FloatField(choices=SIZE_CHOICES, blank=True, null=True)
    length = models.FloatField(choices=GIANT_SIZE_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return '%s, %s, %s, %s' %(
            self.user, self.transit_arrangement, self.model_of_car,
            self.make_of_car
            )

class Bike(models.Model):
    bike_photo = models.ImageField(upload_to="bike_images", blank=True, null=True)
    bike_name = models.CharField(max_length=30)
    bike_frame_size_inches = models.IntegerField()
    bike_owner = models.ForeignKey(User, null=True, blank=True)
    owners_last_year_on_playa = models.IntegerField(default=1)
    stored_in_truck = models.BooleanField(default=True)
    needs_repairs = models.BooleanField(default=False)
    repair_needed = models.CharField(max_length=30, choices=Bike_repairs, null=True, blank=True)
    in_bike_pool_this_year = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    notes = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return '%s %s %s'%(
            self.bike_name, self.bike_owner, self.needs_repairs)

class BicycleMutationInventory(models.Model):
    material = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    units = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s %s %s'%(self.material, self.quantity, self.units)

class BikeMutationSchedule(models.Model):
    event = models.ForeignKey(Event)
    shift = models.CharField(max_length=25, choices=PYB_shifts)
    worker = models.ForeignKey(User, null=True, blank=True, default=None)
    date = models.DateField()

    def __unicode__(self):
        return '%s %s %s' % (self.shift, self.worker, self.date)

class Inventory(models.Model):
    item = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    needs_repairs = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return '%s %s'%(self.item, self.quantity, self.needs_repairs)


