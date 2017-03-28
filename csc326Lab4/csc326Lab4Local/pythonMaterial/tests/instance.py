class A(object):
	pass

class B(A):
	pass

class C(B):
	pass

a = A()
b = B()
c = C()

print "isinstance(object,object): {}".format(isinstance(object,object))
print "isinstance(type,object): {}".format(isinstance(type,object))#weird
print "issubclass(type,object): {}".format(issubclass(type,object))
print "issubclass(A,object): {}".format(issubclass(A,object))

print "issubclass(B,A): {}".format(issubclass(B,A))

print "issubclass(C,A): {}".format(issubclass(C,A))

#since tuple here
print "isinstance((1,2,3),list): {}".format(isinstance((1,2,3),list))

#i think because B derived from A
print "isinstance(a,B): {}".format(isinstance(a,B))
#print "issubclass(a,B): {}".format(issubclass(a,B))


print "isinstance(c,A): {}".format(isinstance(c,A))

#wont work since c, a are both objects. objects not instances of each other
#print "isinstance(c,a): {}".format(isinstance(c,a))
