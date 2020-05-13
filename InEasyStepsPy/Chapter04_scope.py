# chapter 4 - understanding scope
global_var = 1

def my_vars() :
	print('Global variable:', global_var)
	
	local_var = 2
	print('Local variable:', local_var)
	
	global inner_var
	inner_var = 3
	
my_vars()

print('Coerced global:', inner_var)