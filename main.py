import phonenumbers
import vobject

# Export your phone contacts as vcards
with open('contacts.vcf', 'r') as f:
    contacts = vobject.readComponents(f)

    contact_dict = {}

    for contact in contacts:
        try:
            name = contact.fn.value
            tel = phonenumbers.format_number(phonenumbers.parse(contact.tel.value, "DE"), phonenumbers.PhoneNumberFormat.E164)[1:]
            contact_dict[tel] = name
        except KeyError:
            pass
        except AttributeError:
            pass

# Insert leak file here instead of Germany 02.txt
with open("Germany 02.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        tel = line.split(',')[0]
        if tel in contact_dict:
            print("Found match:")
            print(f"{contact_dict[tel]}, +{tel}")
            print(f"{line}")
            print("-----------------------")
            print()