
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
