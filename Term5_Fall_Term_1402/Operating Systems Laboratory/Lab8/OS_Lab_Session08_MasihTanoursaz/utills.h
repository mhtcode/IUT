enum
{
	getStatus = _IO('A', 1),
	changeStatus = _IO('A', 2),
	changePass = _IO('A', 3),
	getContent = _IO('A', 4)
};
struct iut_data
{
	char data[64];
	char password[10];
	char new_password[10];
	char message[64];
};