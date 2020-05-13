
    '''    'userProfile':[
            {'uuid':temp_profile.uuid,
            'gender':temp_profile.gender,
            'role':temp_profile.role,}
        ],
        'userDoc':[
            {'address':temp_doc.address,
            'zipCode':temp_doc.zipCode,
            'citizen':temp_doc.citizen,
            'citizen_Num':temp_doc.citizen_Num,
            'personalCode':temp_doc.personalCode,
            'nationalCode':temp_doc.nationalCode,
            'nationalCardPhoto':str(temp_doc.nationalCardPhoto),
            'date_of_birth':temp_doc.date_of_birth,
            'place_of_birth':temp_doc.place_of_birth,
            'father_name':temp_doc.father_name,
            'father_nationalCode':temp_doc.father_nationalCode,
            'father_pNum':temp_doc.father_pNum,
            'mother_name':temp_doc.mother_name,
            'userPhoto':str(temp_doc.userPhoto),}
        ],'''



                    """    temp_profile = userProfile.objects.get(user_id = item.id)
                        temp_doc = userDoc.objects.get(user_id = item.id) """
                        """
                        # new user created
                        new_user = User()
                        new_user.username = username
                        new_user.email = email
                        new_user.first_name = first_name
                        new_user.last_name = last_name
                        new_user.set_password(password)
                        new_user.save()
                        # new profile created for new user
                        new_profile = userProfile()
                        new_profile.user = new_user
                        new_profile.role = role
                        new_profile.save()
                        # new doc created for new user
                        new_doc = userDoc()
                        new_doc.user = new_user
                        new_doc.gender = gender
                        new_doc.section = section
                        new_doc.address = address
                        new_doc.personalCode = personal_code
                        new_doc.nationalCode = national_code
                        new_doc.father_name = father_name
                        new_doc.father_nationalCode = father_national_code
                        new_doc.userPhoto = user_photo
                        new_doc.nationalCardPhoto = national_card_photo
                        new_doc.mother_name = mother_name
                        new_doc.citizen = citizen
                        new_doc.citizen_Num = citizen_num
                        new_doc.zipCode = zipcode
                        new_doc.date_of_birth = date_birth
                        new_doc.place_of_birth = place_birth
                        new_doc.save()
                        """
