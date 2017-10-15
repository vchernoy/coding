
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

#define DIR_BASE "/tmp/"
#define DIR_FORMAT DIR_BASE "dir-%d/"
#define FILENAME_FORMAT DIR_FORMAT "file-%d.txt"
#define VAL_SIZE (30)

extern int errno;


// reads the variable from the file system.
static void get(const char name[], char value[]) {
    char filename[100];
    int hash, i, len;
    FILE* fp = NULL;
  
    len = strlen(name);
    hash = 0;
    for (i = 0; i < len; i++) {
        hash = hash * 31 + name[i];
    }

    sprintf(filename, FILENAME_FORMAT, hash % 100, hash / 100);
    fp = fopen(filename, "r");
    if (fp != NULL) {
        fgets(value, VAL_SIZE, fp);
        fclose(fp);
    } else {
        value[0] = '\0';
    }
}

// saves the variable in the file system.
static void set(const char name[], const char value[]) {
    char dirname[100];
    char filename[100];
    int hash, i, len, e;
    FILE* fp = NULL;
    struct stat sb;
  
    len = strlen(name);
    hash = 0;
    for (i = 0; i < len; i++) {
        hash = hash * 31 + name[i];
    }

    sprintf(dirname, DIR_FORMAT, hash % 100);
    sprintf(filename, FILENAME_FORMAT, hash % 100, hash / 100);
    e = stat(dirname, &sb);
    if (e != 0 && errno == ENOENT) {
        e = mkdir(dirname, S_IRWXU);
    }
 
    fp = fopen(filename, "w");
    fputs(value, fp);
    fclose(fp);
}

// finds the variable in the array a if it exists, otherwise it reads it from the file system.
static void find_or_get(char a[][30], int s, int e, const char key[]) {
    int i;
    char* k = NULL;
    char* v = NULL;
    char cmd[300];
    char val[100];

    for (i = e-1; i >= s; i--) {
        strcpy(cmd, a[i]);
        if (cmd[0] == 'S') {
            k = strchr(cmd, ' ');
            k++;
            v = strchr(k, ' ');
            *v = '\0';
            v++;
            if (strcmp(k, key) == 0) {
                strcpy(val, v);
                break;
            }
        }
    }
    if (i < s) {
        get(key, val);
    }
    printf("%s\n", val);
}

void commit(char a[][30], int s, int e) {
    int i;
    char* k = NULL;
    char* v = NULL;
    char cmd[300];

    for (i = s; i < e; i++) {
        strcpy(cmd, a[i]);
        if (cmd[0] == 'S') {
            k = strchr(cmd, ' ');
            k++;
            v = strchr(k, ' ');
            *v = '\0';
            v++;
            // Commiting: k=v
            set(k, v);
        }
    }
}

void keyValue(char a[][30], int n) {
    int i, s;
    char* k = NULL;
    char* v = NULL;
    char cmd[300];

    s = 0;
    for (i = 0; i < n; i++) {
        strcpy(cmd, a[i]);
        if (cmd[0] == 'S') {
        } else if (cmd[0] == 'G') {
            k = strchr(cmd, ' ');
            k++;
            // Getting: k
            find_or_get(a, s, i, k);
        } else if (cmd[0] == 'C') {
            commit(a, s, i);
            s = i + 1;
        }
    }
}


int main() {
    char in1[][30] = {"SET a 1", "SET b 2", "GET a", "COMMIT", "SET b 3"};
    char in2[][30] = {"GET b", "SET b 4"};
    char in3[][30] = {"GET b"};

    keyValue(in1, 5);
    keyValue(in2, 2);
    keyValue(in3, 1);
}


