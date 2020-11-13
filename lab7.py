# Donovan Stark(drs474@nau.edu)


def new_contact_store():
    return []


def add_new_contact(contacts, fn, ln, em, pn, bday):
    contacts += [[fn, ln, em, pn, bday]]
    return contacts


def has_contact(contacts, fn, ln):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            return True
    return False


def get_contact_string(contacts, fn, ln):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            return contacts[i]


def remove_contact(contacts, fn, ln):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            del contacts[i]
            return contacts


def update_contact_first_name(contacts, fn, ln, nv):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            contacts[i][0] = nv
    return contacts


def update_contact_last_name(contacts, fn, ln, nv):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            contacts[i][1] = nv
    return contacts


def update_contact_email(contacts, fn, ln, nv):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            contacts[i][2] = nv
    return contacts


def update_contact_phone_number(contacts, fn, ln, nv):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            contacts[i][3] = nv
    return contacts


def update_contact_birthday(contacts, fn, ln, nv):
    for i in range(len(contacts)):
        if fn and ln in contacts[i]:
            contacts[i][4] = nv
    return contacts
