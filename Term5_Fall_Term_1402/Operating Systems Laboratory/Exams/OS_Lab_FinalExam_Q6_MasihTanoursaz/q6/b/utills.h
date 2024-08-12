enum
{
	do_fill = _IO('A', 1),
	do_get = _IO('B', 2),
};

struct iut_data
{
	int sum;
};

struct shm_struct
{
	int done;
};