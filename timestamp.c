#include <stdio.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <time.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <sys/utsname.h>

int main( int argc, char **argv)
{
	struct utsname buf;

	if( uname(&buf) == -1)
	{
		perror("Uname");
	}
	printf("Nom de la machine : %s\nType de machine : %s\n", buf.nodename, buf.sysname);

	struct stat statfile;
	if( stat("at5.commentaire", &statfile) == -1 )
	{
		if(errno == EACCES)
			printf("Pas de droit sur le fichier\n");
		else
			perror("Stat");
	}

	printf("Taille du fichier : %ld\nUID : %d\nInode : %ld\n", statfile.st_size, statfile.st_uid, statfile.st_ino);

	if(mkdir("Repertoire", 0750) == -1)
		perror("Soucis au niveau de la création du répertoire");


	struct timeval date;
	struct timezone tz;
	gettimeofday(&date, &tz);

	printf("Timestamp : %ld\n", date.tv_sec);

	sleep(1);
	// time.h
	time_t date2;
	time(&date2);

	printf("Timestamp : %ld\n", date2);
}

