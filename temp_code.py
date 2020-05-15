
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


        """    json_data = []

            for item in temp_news:
                json_data.append({
                    'auther_id':item.author_id,
                    'auther_username':item.author.username,
                    'post_id':item.id,
                    'title':item.title,
                    'contact':item.content,
                    'release_date':item.release_date,
                }) """


                    """        news_id = request.data['news_id']
                            title = request.data['title']
                            content = request.data['content']
                            release_date = datetime.now()
                            news_pic = request.FILES['news_pic']

                            News.objects.all().filter(id = news_id).update(title = title,content = content,release_date = release_date,news_pic = news_pic)
                """

"""
                            temp_news = News.objects.get(id = news_id)
                            temp_news.title = news_title
                            temp_news.content = news_content
                            temp_news.pic = news_pic
                            temp_news.release_date = news_release_data
                            temp_news.save()
"""
            """    News.objects.all().filter(id = news_id).update(title = news_title
                ,content = news_content,release_date = news_release_data,pic = news_pic) """


"""
class addNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
             serilized_data = serializers.addNewsSerializer(data=request.data)
             if serilized_data.is_valid():
                 news_title = serilized_data.data.get('title')
                 news_content = serilized_data.data.get('content')
                 news_author_id = serilized_data.data.get('author_id')
                 news_pic = request.FILES['pic']
                 news_release_data = datetime.now()
                 news_author = User.objects.get(id = news_author_id)
             else:
                 message = serilized_data.errors
                 return Response({"status_code":"400" , "error":message,"data":"","message":""},)
             #make instance from news
             new_news = News()
             new_news.title = news_title
             new_news.content = news_content
             new_news.release_date = news_release_data
             new_news.pic = news_pic
             new_news.author = news_author
             new_news.save()
             return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Added Success"},status.HTTP_200_OK)
        except Exception as e:
             trace_back = traceback.format_exc()
             message = str(e) + ' ' + str(trace_back)
             return Response({"status_code":"500" , "error": message,"data":"","message":""},)


class deleteNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            serializer = serializers.deleteNewsSerializer(data=request.data)
            if serializer.is_valid():
                news_id = serializer.data.get('news_id')
                if News.objects.all().filter(id = news_id).exists():
                    News.objects.all().filter(id = news_id).delete()
                else :
                    return Response({"status_code":"500" , "error": "object isn,t exists","data":"","message":""},)
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error":message,"data":"","message":""},)

            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Deleted Success"},status.HTTP_200_OK)
        except:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error":message,"data":"","message":""},)


class editNews(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        try:
            serializer = serializers.editNewsSerializer(data=request.data)
            if serializer.is_valid():
                news_id = serializer.data.get('id')
                news_title = serializer.data.get('title')
                news_content = serializer.data.get('content')
                news_release_data = datetime.now()
                news_pic = request.FILES['pic']
            else:
                message = serializer.errors
                return Response({"status_code":"400" , "error":message,"data":"","message":""},)
            # update object in db
            if News.objects.all().filter(id = news_id).exists():
                temp_news = News.objects.get(id = news_id)
                temp_news.title = news_title
                temp_news.content = news_content
                temp_news.pic = news_pic
                temp_news.release_date = news_release_data
                temp_news.save()
            else:
                return Response({"status_code":"500" , "error": "object isn,t exists","data":"","message":""},)
            return Response({"status_code":"200" , "error":"", "data": "" , "message":"News Updated"},status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)


class allNews(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        try:
            temp_news = News.objects.all()
            serilized_data = serializers.allNewsSerializer(temp_news, many=True)
            json_data = serilized_data.data
            return Response({"status_code":"200" , "error":"", "data": json_data , "message":"" },status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return Response({"status_code":"500" , "error": message,"data":"","message":""},)
"""
