import win32com.client as win32
import datetime
import re

def get_folder_by_name(email, folder_name=""):
    """
    Search for a calendar folder in some email account, logged in outlook app
    NOTE: the folder must be inside the calendar folder, leave 'folder_name' empty to use de default calendar folder

    Example
    -------
    get_folder_by_name('example@example.com', 'Fees and coupons')

    return: COM outlook folder object
    """

    outlook = win32.Dispatch('outlook.application')
    recip = outlook.Session.CreateRecipient(email)

    if folder_name != "":
        for folder in outlook.Session.GetSharedDefaultFolder(recip, 9).Folders:
            if (folder.name == folder_name):
                return folder
    else:
        return outlook.Session.GetSharedDefaultFolder(recip, 9)

    raise Exception("Email or folder not found")


def search_metting_by_title_on_date(subject, email, date, folder_name=""):
    """
    Search for a metting by date and subject title
    NOTE: the folder must be inside the calendar folder, leave 'folder_name' empty to use de default calendar folder

    Example
    -------
    teste.search_metting_by_title_on_date(
        'Event title',
        'example@example.com',
        datetime.date(2020,12,5),
        'My tests folder'
    )

    Return the metting if found or false
    """

    calendar_folder = get_folder_by_name(email, folder_name)

    for item in calendar_folder.Items:
        metting_start = datetime.date(item.start.year, item.start.month, item.start.day)

        if metting_start == date and item.subject == subject:
            return item

    return False


def create_allday_metting(subject, date, body, recipients, sender, folder_name="", send=False, reminder_minutes=10080):
    """
    Create a meeting with all day enabled in a given calendar folder and account
    This function does not repeat mettings, based on 'date' and 'subject'.
    This mean if you create twice, the second one will be send to recipients if some recipient or body change
    NOTE: the folder must be inside the calendar folder, leave 'folder_name' empty to use de default calendar folder

    Example
    -------
    create_allday_metting(
        "Event title",
        datetime.date(2020, 10, 25),
        "My body\nwith line break",
        ["email@hotmail.com", "email2@hotmail.com"], # Just work for outlook or exchange e-mails
        "example@example.com",
        "My tests folder",
        True #True to Send, false to display
    )
    """

    created_metting = search_metting_by_title_on_date(subject, sender, date, folder_name)

    # Create the metting
    if not created_metting:
        calendar_folder = get_folder_by_name(sender, folder_name)
        appointment = calendar_folder.Items.add

        appointment.Subject = subject
        appointment.Start = date.strftime('%Y-%m-%d') + " 08:00"
        appointment.End = date.strftime('%Y-%m-%d') + " 08:30"
        appointment.AllDayEvent = True
        appointment.MeetingStatus = 1
    else:
        appointment = created_metting

    new_recipients = [sender] + recipients
    old_recipients = []
    to_remove = []
    to_add = []

   # Set recipients to be removed
    for idx,r in enumerate(appointment.Recipients):

        # Just work for outlook or exchange e-mails
        addr = r.PropertyAccessor.GetProperty('http://schemas.microsoft.com/mapi/proptag/0x39FE001E')

        # Outlook API remove from index starting by 1
        if addr not in new_recipients:
            to_remove.append(idx+1)

        old_recipients.append(addr)

    to_add = list(set(new_recipients) - set(old_recipients))

    # If nothing change (recipients or body) not send, just return
    if (not to_add) and (not to_remove) and (re.sub(r'\s', '', appointment.Body) == re.sub(r'\s', '', body)):
        return

    # Add or update the body
    appointment.Body = body

    # Remove the recipients
    for idx in to_remove:
        appointment.Recipients.Remove(idx)

    # Add the recipients to share the event
    for email in to_add:
        appointment.Recipients.Add(email)

    # Set the reminder
    appointment.ReminderOverrideDefault = True
    appointment.ReminderSet = True
    appointment.ReminderMinutesBeforeStart = reminder_minutes

    if send:
        appointment.Send()
    else:
        appointment.Display()
