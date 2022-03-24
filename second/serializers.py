from rest_framework import serializers
from second.models import Post, Comment

# using model serializer 
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id', 'title', 'desc') #'__all__'  # or fields = [‘field1’, ‘field2’,…...]

class CommentSerializer(serializers.ModelSerializer):
	post = PostSerializer()
	
	class Meta:
		model = Comment
		fields ='__all__'  # or fields = [‘field1’, ‘field2’,…...]

	def create(self, validated_data):
		post_data = validated_data.pop('post') # remove the 'post' data
		pst = Post.objects.create(**post_data) # create the Post objects
		comment = Comment.objects.create(post=pst, **validated_data) # create Comment objects
		return comment

	def update(self, instance, validated_data):
		post_data = validated_data.pop('post') # remove the 'post' data
		# print(f"post_data,{post_data}, validate_data: {validated_data}")
		# update Post model 
		pst = Post.objects.get(id=instance.id)
		pst.title = post_data.get('title', pst.title)
		pst.desc = post_data.get('desc', pst.desc)
		pst.save()
		# update Comment model
		instance.comment = validated_data.get('comment', instance.comment )
		instance.save()
		return instance
