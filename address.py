#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Dec. 12, 2022
# This program prints a Canadian mailing address


def format_address(
    name, street_number, street_name, city, province, postal, apartment_number=None
):
    # Body code executed if the user does not live in an apartment
    if apartment_number == None:
        mailing_address = (
            f"{name}\n{street_number} {street_name}\n{city} {province} {postal}".upper()
        )
        return mailing_address

    # Body code executed if the user does live in an apartment
    else:
        mailing_address = f"{name}\n{apartment_number}-{street_number} {street_name}\n{city} {province} {postal}".upper()
        return mailing_address


def main():
    # Gets the address information from the user
    user_fname = input("Enter your full name: ")
    apartment = input("Do you live in an apartment (y/n): ")

    # Asks the user to enter their apartment number if they live in
    # an apartment

    if apartment == "":
        input("You must enter 'y' or 'n'\nPlease restart.")
    elif apartment[0].lower() == "y":
        apartment_num_user = input("Enter your apartment number: ")

    street_number_u = input("Enter your street number: ")
    street_name_u = input("Enter your street name AND type (Main St., Flower Cres.): ")
    city_user = input("Enter your city: ")
    province_user = input("Enter your province as an abbreviation: ")
    postal_user = input("Enter your postal code: ")

    # Passes argument with apartment number if the user lives in
    # an apartment
    if apartment[0].lower() == "y":

        print(
            format_address(
                user_fname,
                street_number_u,
                street_name_u,
                city_user,
                province_user,
                postal_user,
                apartment_num_user,
            )
        )

    # Passes arguments without apartment number if the user does not live
    # in an apartment
    else:
        print(
            format_address(
                user_fname,
                street_number_u,
                street_name_u,
                city_user,
                province_user,
                postal_user,
            )
        )


if __name__ == "__main__":
    main()
