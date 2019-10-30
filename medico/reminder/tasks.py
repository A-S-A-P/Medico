from __future__ import absolute_import


from django.conf import settings
from twilio.rest import Client

from .models import ReminderDB, Profile
from datetime import datetime, timedelta
from threading import Timer



# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
account_sid = "AC5aac77251da6c5ad23ae623b25d0489f"
auth_token = "a7811229f8225dc01f6d6e046cf14727"
client = Client(account_sid, auth_token)



def send_phone_reminder(appointment_id):
    """Send a reminder to a phone using Twilio Caller"""
    # Get our appointment from the database
    try:
        appointment = ReminderDB.objects.get(pk=appointment_id)
    except:
        # The appointment we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    appointment_time = appointment.hour
    try:
        obj = Profile.objects.get(user=appointment.user)

        print(obj.phone)
        number = + obj.phone
        call = client.calls.create(
        to= "+91" + str(number),
        from_="+12078036264",
        url="http://demo.twilio.com/docs/voice.xml"
        )
        print(call.sid)
        
    

    except Profile.DoesNotExist:
        print("No phone number!")

    appointment.repeat = appointment.repeat - 1
    if appointment.repeat == 0:
        appointment.delete()
    else:
        print("Repeating above for ", appointment.repeat, " more days.")


def schedule_reminder(obj):
    """Schedule a Dramatiq task to send a reminder for this appointment"""

    # Calculate the correct time to send this reminder
    #appointment_time = obj.hour

    # Schedule the Dramatiq task
    from .tasks import send_phone_reminder
    result = send_phone_reminder(obj.pk)

    current_time =datetime.today()
    reminder_time = current_time.replace( hour=obj.hour.hour, minute=obj.hour.minute ) + timedelta(days=1)
    if(reminder_time < current_time):
        delta_t = timedelta(hours=24) - ( current_time - reminder_time )
    else:
        delta_t = reminder_time - current_time 

    secs = delta_t.total_seconds()
    t = Timer(secs, schedule_reminder, [obj])
    t.start()
    print("Refreshed Reminder set for ", obj.id)

    #return result.options['redis_message_id']
    return




def startup():
    
    reminders = ReminderDB.objects.all()

    for item in reminders:
        
        print(item.id)
        print("Time:", item.hour.hour, " : ", item.hour.minute)
        current_time =datetime.today()
        reminder_time = current_time.replace( hour=item.hour.hour, minute=item.hour.minute ) 
        if(reminder_time < current_time):
            delta_t = timedelta(hours=24) - ( current_time - reminder_time )
        else:
            delta_t = reminder_time - current_time 
        secs = delta_t.total_seconds()
        print("Executing in tminus: ", secs, "or, hours:", secs/3600)
        t = Timer(secs, schedule_reminder, [item])
        t.start()

        #schedule_reminder(item)
        print("Reminder set for ", item.id, item.name)
