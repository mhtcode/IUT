#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

// Define parts
#define Max 100
#define MAX_LEN 128
#define ANSI_COLOR_RED "\x1b[31m"
#define ANSI_COLOR_GREEN "\x1b[32m"
#define ANSI_COLOR_YELLOW "\x1b[33m"
#define ANSI_COLOR_BLUE "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN "\x1b[36m"
#define ANSI_COLOR_RESET "\x1b[0m"
#define newblue "\e[1;34m"
#define BHGRN "\e[1;92m"

int first = 1, second = 4;        // = 6
int lower = 1100, upper = 1200;   // Rand ID for team
int lower1 = 1201, upper1 = 2001; // Rand ID for palyer

// Structures
typedef struct teams
{
    int ID;
    char name[20];
    char coachmail[100];
    char password[100];
    int Money;
    int CUPS;
    int played;
    int won;
    int drawn;
    int lost;
    int gf;
    int gd;
    int ga;
    int points;
    int player_count;
    int mplayer_count;
    struct Players
    {
        int P_ID;
        char P_name[20];
        int P_Atacking_power;
        int P_defencing_power;
        int P_value;
        char P_STATUS[20];
    } players[8];
    struct matchplayers
    {
        int m_ID;
        char m_name[20];
        int m_Atacking_power;
        int m_defencing_power;
        int m_value;
        char m_STATUS[20];
    } mplayer[5];

} stp;

typedef struct players
{
    int ID;
    char name[50];
    int Atacking_power;
    int Defencing_power;
    int value;
    char status[50];

} player;

typedef struct transfer_window
{
    char status[10];
    int entery;
} twl;
typedef struct matches_schedule
{
    int red_team_ID;
    int blue_team_ID;
    int blue_team_atck;
    int blue_team_defence;
    int red_team_atck;
    int red_team_defense;
    float red_team_goals;
    float blue_team_goals;
    char blue_teamname[20];
    char red_teamname[20];
    int week;
} sms;
// Functions
// Print Functions

void printf_red1(const char *s)
{
    printf("\033[0m\033[1;31m%s\033[0m", s);
}

void printf_green1(const char *s)
{
    printf("\033[0m\033[1;32m%s\033[0m", s);
}

void printf_yellow1(const char *s)
{
    printf("\033[0m\033[1;33m%s\033[0m", s);
}

void printf_blue1(const char *s)
{
    printf("\033[0m\033[1;34m%s\033[0m", s);
}

void printf_pink1(const char *s)
{
    printf("\033[0m\033[1;35m%s\033[0m", s);
}

void printf_cyan1(const char *s)
{
    printf("\033[0m\033[1;36m%s\033[0m", s);
}

// Void Functions
void image(char *txt, int color, int how);
void print_image(FILE *fptr, int color, int how);
void enter();
void enter1();
void vorood();
void ForgotPassword();
void adminpage();
void Add_team();
void Add_Player();
void Show_Teams();
void Show_players();
void Central_core();
void Coahcpage(char *name);
void Buy_a_Player(char *name);
void Sell_a_Player(char *name);
int submit_squad_check(char *name);
void submit_squad(char *name);
void select_squad(char *name);
void League_Standing(char *name);
void Fixtures(char *name);
void Upcoming_Opponent(char *name);
void Change_password();
void namepass_update();
void namepass_update_change();
void Show_Teams_temp();
void change_detail_team();
void change_detail_player();
void sort_by_points();
void sort_player();
void start_league();
void sow_teams_ready();
void start_week();
void end_season();
void update_powers(int rno1);
void update_winner(int rno1);
void update_loser(int rno1);
void update_draw(int rno1);
void League_Standing_forend();
void update_cup(int rno1);

// Int Functions
int ID_check_team(int id);
int name_check_team(char *name);
int ID_check_player(int id);
int namepass_check_signin(char *name, char *pass);
int namepass_check_update(char *name, char *pass);
int namepass_check_update_forgot(char *name, char *pass);
int namepass_check_update_change(char *coachmail, char *pass);
int Show_players_for_buy();
int Show_players_for_sell(char *name);
int show_players_of_team(char *name);
int show_players_of_team_for_match(char *name);
int transfer_window();
int check_season();
int show_teams_for_league();

// MAIN Function
int main()
{
    enter();
    return 0;
}

// Login page
void enter() // pass
{
    int flag = 0;
    twl t;
    FILE *fp = fopen("transfer_window.txt", "a+");
    while (fread(&t, sizeof(twl), 1, fp))
    {
        flag = 1;
    }
    if (flag == 0)
    {
        t.entery = 1;
        strcpy(t.status, "open");
        fwrite(&t, sizeof(twl), 1, fp);
    }
    fclose(fp);
    image("welcome.txt", 4, 1);
    printf("\n\n");
    image("image.txt", 4, 1);
    printf("\a\n\n");
    printf(ANSI_COLOR_GREEN "Enter your choice ->\t1: Sign in\t2: Forgot your password?\t\t0: EXIT \nNumber is : " ANSI_COLOR_RESET);

    int input;
    scanf("%d", &input);
    printf("\n");
    if (input == 1)
        vorood();
    else if (input == 2)
        ForgotPassword();
    else if (input == 0)
        exit(1);
    else
        enter1();
}
void enter1() // pass
{
    printf(ANSI_COLOR_YELLOW "\nYou are in login page.\n\a\n" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_GREEN "Enter your choice ->\t1: Sign in\t2: Forgot your password?\t\t0: EXIT \nNumber is : " ANSI_COLOR_RESET);

    int input;
    scanf("%d", &input);
    printf("\n");
    if (input == 1)
        vorood();
    else if (input == 2)
        ForgotPassword();
    else if (input == 0)
        exit(1);
    else
        enter1();
}
void vorood() // pass
{
    char teamname[Max];
    char password[Max];
    printf(ANSI_COLOR_CYAN "Enter the username for sign in:\n" ANSI_COLOR_RESET);
    scanf("%s", &teamname);
    printf(ANSI_COLOR_CYAN "Enter Your password:\n" ANSI_COLOR_RESET);
    scanf("%s", &password);
    if (strcmp(teamname, "Admin") == 0 && strcmp(password, "Admin") == 0)
    {
        adminpage();
    }
    else if (namepass_check_signin(teamname, password))
    {
        Coahcpage(teamname);
    }
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username not defineded; try again please. **\n\n\a" ANSI_COLOR_RESET);
        enter1();
    }
    return;
}
void ForgotPassword() // pass
{
    char teamname[Max];
    char password[Max];
    printf(ANSI_COLOR_CYAN "Enter the username to change password :\n" ANSI_COLOR_RESET);
    scanf("%s", &teamname);
    printf(ANSI_COLOR_CYAN "Enter the mail of coach :\n" ANSI_COLOR_RESET);
    scanf("%s", &password);
    if (namepass_check_update_forgot(teamname, password))
    {
        namepass_update(teamname);
    }
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match email of coach. **\n\n\a" ANSI_COLOR_RESET);
    }

    enter1();
    return;
}
void image(char *txt, int color, int how)
{
    char *filename = txt;
    FILE *fptr = NULL;

    if ((fptr = fopen(filename, "r")) == NULL)
    {
        fprintf(stderr, "error opening %s\n", filename);
        exit(1);
    }

    print_image(fptr, color, how);

    fclose(fptr);
}
void print_image(FILE *fptr, int color, int how)
{
    char read_string[MAX_LEN];

    if (how == 1)
    {
        while (fgets(read_string, sizeof(read_string), fptr) != NULL)
        {
            switch (color)
            {
            case 1:
                printf(ANSI_COLOR_BLUE "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 2:
                printf(ANSI_COLOR_RED "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 3:
                printf(ANSI_COLOR_YELLOW "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 4:
                printf(ANSI_COLOR_MAGENTA "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 5:
                printf(ANSI_COLOR_CYAN "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 6:
                printf(ANSI_COLOR_GREEN "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 7:
                printf(newblue "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 8:
                printf(BHGRN "%s" ANSI_COLOR_RESET, read_string);
                break;
            }
            color++;
            if (color > 8)
                color %= 8;
        }
    }
    else
    {
        while (fgets(read_string, sizeof(read_string), fptr) != NULL)
        {
            switch (color)
            {
            case 1:
                printf(ANSI_COLOR_BLUE "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 2:
                printf(ANSI_COLOR_RED "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 3:
                printf(ANSI_COLOR_YELLOW "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 4:
                printf(ANSI_COLOR_MAGENTA "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 5:
                printf(ANSI_COLOR_CYAN "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 6:
                printf(ANSI_COLOR_GREEN "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 7:
                printf(newblue "%s" ANSI_COLOR_RESET, read_string);
                break;
            case 8:
                printf(BHGRN "%s" ANSI_COLOR_RESET, read_string);
                break;
            }
        }
    }
}

// Admin page
void adminpage()
{
    printf(ANSI_COLOR_YELLOW "\nYou are in admin page.\n\a\n" ANSI_COLOR_RESET);
    int input = 0;
    while (1)
    {
        printf(ANSI_COLOR_GREEN "Enter your choice ->\t1: Add Team\t2: Add Player\t3: Show Teams\t4: Show Players\t\t5: Central core\t\t6: change_detail_team\t\t7: Exit\nNumber is : " ANSI_COLOR_RESET);
        scanf("%d", &input);
        switch (input)
        {
        case 1: // pass
            Add_team();
            break;
        case 2: // pass
            Add_Player();
            break;
        case 3: // pass
            Show_Teams();
            break;
        case 4: // pass

            Show_players();
            break;
        case 5:
            Central_core();
            break;
        case 6: // pass
            change_detail_team();
            break;

        case 7: // pass
            enter1();
            break;
        default:
            enter1();
            break;
        }
        return;
    }
}
void Add_team() // pass
{
    srand(time(0));
    int rnd = ((rand() % (upper - lower + 1)) + lower);

    stp tp;
    FILE *fp;
    fp = fopen("team_info.txt", "a+");

    tp.ID = ID_check_team(rnd);
    printf(ANSI_COLOR_YELLOW "\nTeam ID is %d\n" ANSI_COLOR_RESET, tp.ID);
    do
    {
        printf(ANSI_COLOR_CYAN "\nEnter team name : " ANSI_COLOR_RESET);
        scanf("%s", tp.name);
    } while (!name_check_team(tp.name));

    tp.drawn = 0;
    tp.ga = 0;
    tp.gd = 0;
    tp.gf = 0;
    tp.won = 0;
    tp.CUPS = 0;
    tp.played = 0;
    tp.Money = 100;
    tp.player_count = 0;
    tp.mplayer_count = 0;
    tp.points = 0;
    tp.lost = 0;

    printf(ANSI_COLOR_CYAN "Enter email of COACH : " ANSI_COLOR_RESET);
    scanf("%s", tp.coachmail);

    strcpy(tp.password, tp.coachmail);

    fwrite(&tp, sizeof(stp), 1, fp);

    fclose(fp);

    adminpage();
}
void Add_Player() // pass
{
    srand(time(0));
    int rnd = ((rand() % (upper1 - lower1 + 1)) + lower1);
    player p;
    FILE *fp;
    fp = fopen("players_info.txt", "a+");

    p.ID = ID_check_player(rnd);
    printf(ANSI_COLOR_YELLOW "\nPlayer ID is %d\n" ANSI_COLOR_RESET, p.ID);

    printf(ANSI_COLOR_CYAN "\nEnter player name : " ANSI_COLOR_RESET);
    scanf("%s", p.name);
    do
    {
        printf(ANSI_COLOR_CYAN "Enter Atacking_power of player : " ANSI_COLOR_RESET);
        scanf("%d", &p.Atacking_power);
        printf(ANSI_COLOR_CYAN "Enter Defencing_power of player : " ANSI_COLOR_RESET);
        scanf("%d", &p.Defencing_power);

    } while (!((0 < p.Atacking_power < 101) && (0 < p.Atacking_power < 101)));
    do
    {
        printf(ANSI_COLOR_CYAN "Enter Value of player : " ANSI_COLOR_RESET);
        scanf("%d", &p.value);
    } while (!(9 < p.value < 21));

    strcpy(p.status, "Free Agent");

    if (p.ID != 0)
        fwrite(&p, sizeof(player), 1, fp);

    fclose(fp);

    adminpage();
}
void Show_Teams() // pass
{
    image("showteam.txt", 7, 0);
    printf("\n");
    stp tp;
    FILE *fp;
    int rno;
    char name[50];
    int flag = 0;
    fp = fopen("team_info.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-30s%-30s%-10s%-10s", "ID", "Name", "Coach-mail", "Money", "CUPS" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-30s%-30s%-10s%-10s", "--", "----", "----------", "-----", "----" ANSI_COLOR_RESET);

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        printf(ANSI_COLOR_YELLOW "\n%-10d%-30s%-30s%-10d%-5d" ANSI_COLOR_RESET, tp.ID, tp.name, tp.coachmail, tp.Money, tp.CUPS);
        printf("\n------------------------------------------------------------------------------------------");
    }
    printf("\n\n");
    fclose(fp);
    fp = fopen("team_info.txt", "r");

    printf(ANSI_COLOR_CYAN "\nEnter the ID of the desired team : \n" ANSI_COLOR_RESET);
    scanf("%d", &rno);
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno)
        {
            strcpy(name, tp.name);
            flag = 1;
        }
    }
    if (flag)
    {
        if (show_players_of_team(name))
            adminpage();
        else
        {
            printf_red1("\n\a\nERROR : ** There is no player for this team. **\n");
            int ex = 0;
            printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number !!\nNumber is : " ANSI_COLOR_RESET);
            scanf("%d", &ex);
            if (ex == 1)
                adminpage();

            Show_Teams();
        }
    }
    else
    {
        printf_red1("\n\aERROR : ** ID not identified. **\n");
        int ex = 0;

        printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number !!\nNumber is : " ANSI_COLOR_RESET);
        scanf("%d", &ex);
        if (ex == 1)
            adminpage();

        Show_Teams();
    }

    fclose(fp);
    adminpage();
}
void Show_players() // pass
{
    printf("\n");
    image("showplayer.txt", 4, 0);
    sort_player();
    player p1;
    FILE *fp;
    int flag = 0;
    fp = fopen("players_info.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-30s%-30s%-20s%-10s", "ID", "Name", "Atacking_power", "Defencing_power", "Status", "Value" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-20s%-30s%-30s%-20s%-10s", "--", "----", "--------------", "---------------", "------", "-----" ANSI_COLOR_RESET);

    while (fread(&p1, sizeof(player), 1, fp))
    {
        printf(ANSI_COLOR_YELLOW "\n%-10d%-20s%-30d%-30d%-20s%-10d " ANSI_COLOR_RESET, p1.ID, p1.name, p1.Atacking_power, p1.Defencing_power, p1.status, p1.value);
        printf_cyan1("\n---------------------------------------------------------------------------------------------------------------------");
        flag++;
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of players: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
    adminpage();
}
void Central_core()
{
    printf(ANSI_COLOR_YELLOW "\nYou are in central core page.\n\a\n" ANSI_COLOR_RESET);

    int input = 0;
    printf(ANSI_COLOR_GREEN "Enter your choice ->\t1: Start_league\t\t2: Open / Close Transfer Window\t\t3: Start Week i-th Games\t\t4: End Season and Announce The Champion\t\t\t5: Exit\nNumber is : " ANSI_COLOR_RESET);
    scanf("%d", &input);
    switch (input)
    {
    case 1:
        start_league();
        break;
    case 2:
        transfer_window();
        break;
    case 3:
        start_week();
        break;
    case 4:
        end_season();
        break;
    default:
        adminpage();
        break;
    }
}
void change_detail_team() // pass
{
    stp tp;
    FILE *fp, *fp1;
    Show_Teams_temp();
    printf("\n\n\a");
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");
    printf("Enter ID to update : ");
    int j, rno1, found = 0;
    scanf("%d", &rno1);
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;

            fflush(stdin);
            printf_cyan1("\nEnter new Name : ");
            scanf("%[^\n]s", tp.name);
            printf_cyan1("\nEnter new coachmail to update: ");
            scanf("%s", tp.coachmail);
            printf_cyan1("\nEnter new password to update : ");
            scanf("%s", tp.password);
            printf_cyan1("\nEnter new cups to update : ");
            scanf("%d", &tp.CUPS);
            printf_cyan1("\nEnter new played to update : ");
            scanf("%d", &tp.played);
            printf_cyan1("\nEnter new won to update : ");
            scanf("%d", &tp.won);
            printf_cyan1("\nEnter new drawn to update : ");
            scanf("%d", &tp.drawn);
            printf_cyan1("\nEnter new lost to update : ");
            scanf("%d", &tp.lost);
            printf_cyan1("\nEnter new gd to update : ");
            scanf("%d", &tp.gd);
            printf_cyan1("\nEnter new ga to update : ");
            scanf("%d", &tp.ga);
            printf_cyan1("\nEnter new points to update : ");
            scanf("%d", &tp.points);
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf_red1("\n\aERROR : ** Team Not Found **");
    printf("\n");

    adminpage();
}
void sort_player() // pass
{
    player *s, s1;
    FILE *fp;
    fp = fopen("players_info.txt", "r");
    fseek(fp, 0, SEEK_END);
    int n = ftell(fp) / sizeof(player);
    s = (player *)calloc(n, sizeof(player));

    rewind(fp);
    for (int i = 0; i < n; i++)
    {
        fread(&s[i], sizeof(player), 1, fp);
    }
    fclose(fp);
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if ((s[i].Atacking_power + s[i].Defencing_power) / s[i].value < (s[j].Atacking_power + s[j].Defencing_power) / s[j].value)
            {
                s1 = s[i];
                s[i] = s[j];
                s[j] = s1;
            }
        }
    }

    fp = fopen("players_info.txt", "w");
    for (int i = 0; i < n; i++)
    {

        fwrite(&s[i], sizeof(player), 1, fp);
    }
    fclose(fp);
    printf("\n");
}

// Coach page
void Coahcpage(char *name)
{
    image("coachpageimage.txt", 1, 0);
    printf("\n\n");
    printf(ANSI_COLOR_YELLOW "\nYou are in coach page of %s .\n\a\n" ANSI_COLOR_RESET, name);
    int input = 0;
    while (1)
    {
        printf(ANSI_COLOR_GREEN "Enter your choice ->\t1: Buy a Player   \t2: Sell a Player\t3: Select Squad (Submit Squad)\t4: League Standing\t5: Fixtures\t6: Upcoming Opponent\t7: Change Password\t8: Exit\n" ANSI_COLOR_RESET);
        printf(ANSI_COLOR_GREEN "Number is : " ANSI_COLOR_RESET);
        scanf("%d", &input);
        switch (input) // pass
        {
        case 1:
            if (transfer_window())
                Buy_a_Player(name);
            else
            {
                printf_red1("\nERROR: ** The transfer window is closed now. **\n\a");
                Coahcpage(name);
            }
            break;
        case 2:
            if (transfer_window())
                Sell_a_Player(name);
            else
            {
                printf_red1("\nERROR: ** The transfer window is closed now. **\n\a");
                Coahcpage(name);
            }
            break;
        case 3:
            if (submit_squad_check(name))
                select_squad(name);
            else
                submit_squad(name);
            break;
        case 4:
            sort_by_points();
            League_Standing(name);
            break;
        case 5:
            Fixtures(name);
            break;
        case 6:
            Upcoming_Opponent(name);
            break;
        case 7: // pass
            Change_password();
            break;
        case 8:
            enter1();
            break;
        default:
            enter1();
            break;
        }
    }
}
void Buy_a_Player(char *name) // pass
{
    stp tp;
    player p;
    FILE *fp = fopen("team_info.txt", "r");
    FILE *fpp = fopen("players_info.txt", "r");
    FILE *fp1 = fopen("temp_player.txt", "w");
    FILE *fp2 = fopen("temp_team.txt", "w");
    int check = 0;

    if (Show_players_for_buy(name))
    {
        while (fread(&tp, sizeof(stp), 1, fp))
        {
            if (strcmp(tp.name, name) == 0)
            {

                int rno;

                printf(ANSI_COLOR_CYAN "\nEnter the ID of player that you want to buy: " ANSI_COLOR_RESET);
                scanf("%d", &rno);
                while (fread(&p, sizeof(player), 1, fpp))
                {
                    if (rno == p.ID)
                    {
                        check = 1;
                        if (p.value <= tp.Money)
                        {
                            char yesorno[5];
                            printf(ANSI_COLOR_CYAN "\n\aAre you sure about buying %s at a price of %d $ ? " ANSI_COLOR_RESET, p.name, p.value);
                            scanf("%s", strlwr(yesorno));
                            strcpy(yesorno, strlwr(yesorno));
                            if (strcmp(yesorno, "yes") == 0)
                            {
                                strcpy(p.status, name);

                                tp.players[tp.player_count].P_ID = p.ID;
                                strcpy(tp.players[tp.player_count].P_name, p.name);
                                tp.players[tp.player_count].P_Atacking_power = p.Atacking_power;
                                tp.players[tp.player_count].P_defencing_power = p.Defencing_power;
                                tp.players[tp.player_count].P_value = p.value;
                                strcpy(tp.players[tp.player_count].P_STATUS, p.status);

                                tp.Money -= p.value;
                                tp.player_count += 1;
                            }
                            else
                            {
                                Coahcpage(name);
                            }
                        }
                        else
                        {
                            int ex = 0;
                            printf_red1("\nERROR : ** Sorry you don't have enough money to buy this player. **\n\a");
                            printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number !!\nNumber is : " ANSI_COLOR_RESET);
                            scanf("%d", &ex);
                            if (ex == 1)
                                Coahcpage(name);
                            Buy_a_Player(name);
                        } // else

                    } // if

                    fwrite(&p, sizeof(player), 1, fp1);
                } // while

            } // if
            fwrite(&tp, sizeof(stp), 1, fp2);
        } // While loop
        // Show_Teams_temp();

        fclose(fp);
        fclose(fpp);
        fclose(fp1);
        fclose(fp2);
        if (check == 1)
        {
            FILE *fp1 = fopen("temp_player.txt", "r");
            FILE *fpp = fopen("players_info.txt", "w");
            while (fread(&p, sizeof(player), 1, fp1))
            {
                fwrite(&p, sizeof(player), 1, fpp);
            }

            FILE *fp2 = fopen("temp_team.txt", "r");
            FILE *fp = fopen("team_info.txt", "w");
            while (fread(&tp, sizeof(stp), 1, fp2))
            {
                fwrite(&tp, sizeof(stp), 1, fp);
            }

            fclose(fp);
            fclose(fpp);
            fclose(fp1);
            fclose(fp2);
            Show_Teams_temp();
        }
        else
        {
            printf_red1("\n\aERROR : ** ID not identified. **\n");
            int ex = 0;

            printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number !!\nNumber is : " ANSI_COLOR_RESET);
            scanf("%d", &ex);
            if (ex == 1)
                Coahcpage(name);

            Buy_a_Player(name);
        }
    }
    else
    {
        printf_red1("\n\a\n\nERROR : ** There is no player to buy. **");
    }

    Coahcpage(name);
}
void Sell_a_Player(char *name) // pass
{
    stp tp;
    player p;
    FILE *fp = fopen("team_info.txt", "r");
    FILE *fpp = fopen("players_info.txt", "r");
    FILE *fp1 = fopen("temp_player.txt", "w");
    FILE *fp2 = fopen("temp_team.txt", "w");
    int check = 0;
    if (Show_players_for_sell(name))
    {
        while (fread(&tp, sizeof(stp), 1, fp))
        {
            if (strcmp(tp.name, name) == 0)
            {

                int rno;

                printf(ANSI_COLOR_CYAN "\nEnter the ID of player that you want to sell: " ANSI_COLOR_RESET);
                scanf("%d", &rno);
                while (fread(&p, sizeof(player), 1, fpp))
                {
                    if (rno == p.ID)
                    {
                        check = 1;
                        char yesorno[5];
                        printf(ANSI_COLOR_CYAN "\n\aAre you sure about selling %s at a price of %d ? " ANSI_COLOR_RESET, p.name, p.value);
                        scanf("%s", strlwr(yesorno));
                        strcpy(yesorno, strlwr(yesorno));
                        if (strcmp(yesorno, "yes") == 0)
                        {
                            strcpy(p.status, "Free Agent");

                            strcpy(tp.players[tp.player_count].P_STATUS, p.status);

                            tp.Money += p.value;
                            tp.player_count -= 1;
                        }
                        else
                        {
                            Coahcpage(name);
                        }

                    } // if

                    fwrite(&p, sizeof(player), 1, fp1);
                } // while

            } // if
            fwrite(&tp, sizeof(stp), 1, fp2);
        } // While loop

        fclose(fp);
        fclose(fpp);
        fclose(fp1);
        fclose(fp2);
        if (check == 1)
        {
            FILE *fp1 = fopen("temp_player.txt", "r");
            FILE *fpp = fopen("players_info.txt", "w");
            while (fread(&p, sizeof(player), 1, fp1))
            {
                fwrite(&p, sizeof(player), 1, fpp);
            }

            FILE *fp2 = fopen("temp_team.txt", "r");
            FILE *fp = fopen("team_info.txt", "w");
            while (fread(&tp, sizeof(stp), 1, fp2))
            {
                fwrite(&tp, sizeof(stp), 1, fp);
            }

            fclose(fp);
            fclose(fpp);
            fclose(fp1);
            fclose(fp2);
            Show_Teams_temp();
        }

        else
        {
            int ex = 0;
            printf_red1("\n\aERROR : ** ID not identified. **\n");

            printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number:\nNumber is : " ANSI_COLOR_RESET);
            scanf("%d", &ex);
            if (ex == 1)
                Coahcpage(name);
            Sell_a_Player(name);
        }
    }
    else
    {
        printf_red1("\n\a\nERROR : ** There is no player to sell. **");
    }

    Coahcpage(name);
}
int submit_squad_check(char *name)
{
    stp tp;
    player p;
    int ready = 0;

    FILE *fpm = fopen("ready_for_match.txt", "a+");
    while (fread(&tp, sizeof(stp), 1, fpm))
    {
        if (strcmp(tp.name, name) == 0)
        {
            ready = 1;
        }
    }

    fclose(fpm);

    return ready;
}
void submit_squad(char *name)
{
    stp tp;
    player p;
    int ready = 0;
    FILE *fp = fopen("team_info.txt", "r");

    FILE *fpm = fopen("ready_for_match.txt", "a+");
    while (fread(&tp, sizeof(stp), 1, fpm))
    {
        if (strcmp(tp.name, name) == 0)
        {
            ready = 1;
        }
    }

    if (ready == 0)
    {
        int check = 0;
        Show_players_for_sell(name);
        while (fread(&tp, sizeof(stp), 1, fp))
        {
            if (strcmp(tp.name, name) == 0)
            {

                if (tp.player_count == 8)
                {
                    char yesorno[5];
                    printf(ANSI_COLOR_CYAN "Are you sure you want to announce readiness? " ANSI_COLOR_RESET);
                    scanf("%s", strlwr(yesorno));
                    strcpy(yesorno, strlwr(yesorno));
                    if (strcmp(yesorno, "yes") == 0)
                    {
                        fwrite(&tp, sizeof(stp), 1, fpm);
                        printf(ANSI_COLOR_YELLOW "\nYour team has been successfully marked readiness.\n" ANSI_COLOR_RESET);
                    }
                    else
                    {
                        Coahcpage(name);
                    }
                }
                else
                {
                    printf_red1("\n\aERROR : ** Not enough players. Buy some players please**\n");
                    Coahcpage(name);
                }

            } // if

        } // While loop
    }
    else
    {
        printf_red1("\n\aERROR : ** You have already declared your readiness**\n");
        Coahcpage(name);
    }
    FILE *fpt = fopen("data_team.txt", "w");
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        fwrite(&tp, sizeof(stp), 1, fpt);
    }
    fclose(fpm);
    fclose(fp);

    Coahcpage(name);
}
void select_squad(char *name)
{

    stp tp;
    player p;
    int temp = 0;
    FILE *fplt = fopen("league_teams.txt", "r");
    while (fread(&tp, sizeof(stp), 1, fplt))
    {
        if (strcmp(name, tp.name) == 0)
        {
            temp = 1;
            fseek(fplt, 0, SEEK_SET);
        }
    }
    if (temp)
    {

        FILE *fp = fopen("team_info.txt", "r");
        FILE *fpp = fopen("players_info.txt", "r");
        FILE *fpm = fopen("matchday.txt", "a");
        int lst_players[5];
        int temp = 0;
        // FILE *fp2 = fopen("temp_team.txt", "w");
        int check = 0;
        int i = 0;
        Show_players_for_sell(name);
        while (fread(&tp, sizeof(stp), 1, fp))
        {
            if (strcmp(tp.name, name) == 0)
            {
                tp.mplayer_count = 0;
                if (tp.player_count == 8)
                {
                    int rno;
                    while (i < 5)
                    {
                        temp = 0;
                        printf(ANSI_COLOR_CYAN "\nEnter the desired player %d ID: " ANSI_COLOR_RESET, i + 1);
                        scanf("%d", &rno);
                        for (int j = 0; j < 5; j++)
                        {
                            if (rno == lst_players[j])
                            {
                                temp = 1;
                            }
                        }
                        if (!temp)
                        {
                            while (fread(&p, sizeof(player), 1, fpp))
                            {
                                if (rno == p.ID)
                                {
                                    check = 1;

                                    strcpy(tp.mplayer[i].m_name, p.name);
                                    strcpy(tp.mplayer[i].m_STATUS, p.status);
                                    tp.mplayer[i].m_ID = p.ID;
                                    tp.mplayer[i].m_Atacking_power = p.Atacking_power;
                                    tp.mplayer[i].m_defencing_power = p.Defencing_power;
                                    tp.mplayer[i].m_value = p.value;
                                    lst_players[i] = p.ID;
                                    tp.mplayer_count += 1;
                                    i++;
                                    fseek(fpp, 0, SEEK_SET);
                                    break;

                                } // if
                            }     // while
                        }
                        if (temp == 1)
                        {
                            printf(ANSI_COLOR_RED "ERROR : ** You have already selected this player.\n **" ANSI_COLOR_RESET);
                        }
                        if (tp.mplayer_count == 5)
                        {
                            fwrite(&tp, sizeof(stp), 1, fpm);
                            break;
                        }
                    }
                }
                else
                {
                    printf_red1("\n\aERROR : ** Not enough players. Buy some players please**\n");
                    Coahcpage(name);
                }

            } // if

        } // While loop

        fclose(fp);
        FILE *fpt = fopen("data_player.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fpp))
        {
            fwrite(&tp, sizeof(stp), 1, fpt);
        }
        fclose(fpt);
        fclose(fpp);
        fclose(fpm);
        if (check == 1)
        {
            if (show_players_of_team_for_match(name) == 5)
            {
                char yesorno[5];
                printf(ANSI_COLOR_CYAN "Are you sure you want to announce readiness? " ANSI_COLOR_RESET);
                scanf("%s", strlwr(yesorno));
                strcpy(yesorno, strlwr(yesorno));
                if (strcmp(yesorno, "yes") == 0)
                {
                    FILE *fpm = fopen("matchday.txt", "r");
                    FILE *fp = fopen("matchteam.txt", "a+");
                    while (fread(&tp, sizeof(stp), 1, fpm))
                    {
                        fwrite(&tp, sizeof(stp), 1, fp);
                    }
                }
                fclose(fp);
                fclose(fpm);
            }
            else
            {
                int ex = 0;
                printf_red1("\n\aERROR : ** Not enough players for match. **\n");

                printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number:\nNumber is : " ANSI_COLOR_RESET);
                scanf("%d", &ex);
                if (ex == 1)
                    Coahcpage(name);
            }
        }

        else
        {
            int ex = 0;
            printf_red1("\n\aERROR : ** ID not identified. **\n");

            printf(ANSI_COLOR_BLUE "\nIf you want to exit, enter the number 1 , otherwise enter another number:\nNumber is : " ANSI_COLOR_RESET);
            scanf("%d", &ex);
            if (ex == 1)
                Coahcpage(name);
            select_squad(name);
        }

        fclose(fp);
        fclose(fpm);
    }
    else
    {
        printf(ANSI_COLOR_RED "\nERROR: ** Unfortunately, you do not participate in the league. **\n" ANSI_COLOR_RESET);
    }
    Coahcpage(name);
}
void League_Standing(char *name) // pass
{
    sort_by_points();
    stp tp;
    FILE *fp = fopen("team_info.txt", "r");
    int rows = 1, columns;
    printf_red1("\n\t\t\tThis is the league table standing.\n\n\a");

    printf_cyan1("    Name\tPlayed\t  Won\tDrawn\tLost\tGF\tGD\tGA\tPoints\n");
    printf("    ----\t------\t  ---\t-----\t---\t--\t--\t--\t------\n\n");
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        switch (rows)
        {
        case 1:
            printf(BHGRN "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 2:
            printf(ANSI_COLOR_GREEN "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 3:
            printf(ANSI_COLOR_YELLOW "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 4:
            printf(ANSI_COLOR_RED "%d : " ANSI_COLOR_RESET, rows);
            break;
        default:
            printf(newblue "%d : " ANSI_COLOR_RESET, rows);
            break;
        }
        while (rows < 5)
        {
            for (columns = 1; columns < 10; columns++)
            {

                switch (columns)
                {
                case 1:
                    if (strcmp(tp.name, name) == 0)
                        printf(ANSI_COLOR_YELLOW "%-10s\t" ANSI_COLOR_RESET, tp.name);
                    else
                        printf(ANSI_COLOR_BLUE "%-10s\t" ANSI_COLOR_RESET, tp.name);
                    break;
                case 2:
                    printf("  %d\t  ", tp.played);
                    break;
                case 3:
                    printf("%d\t", tp.won);
                    break;
                case 4:
                    printf(" %d\t", tp.drawn);
                    break;
                case 5:
                    printf("%d\t", tp.lost);
                    break;
                case 6:
                    printf("%d\t", tp.gf);
                    break;
                case 7:
                    printf("%d\t", tp.gd);
                    break;
                case 8:
                    printf("%d\t", tp.ga);
                    break;
                case 9:
                    printf(ANSI_COLOR_RED "  %d\t\n" ANSI_COLOR_RESET, tp.points);
                    break;
                }
            }

            printf("\n|-------------------------------------------------------------------------------|\n");
            printf("\n");
            rows++;
            break;
        }
    }
}
void Fixtures(char *name)
{
    twl tw;
    FILE *fpt = fopen("league.txt", "r");
    int week;
    int temp = 0;
    char status[10];
    while (fread(&tw, sizeof(tw), 1, fpt))
    {
        week = tw.entery;
        strcpy(status, tw.status);
    }
    fclose(fpt);
    sms s;
    FILE *fplm = fopen("league_matches.txt", "r");
    while (fread(&s, sizeof(sms), 1, fplm))
    {
        if (strcmp(s.blue_teamname, name) == 0)
        {
            printf("\n\n--------------------------------------------------------------");
            printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-20s\n" ANSI_COLOR_RESET, "week", "red_team", "blue_team");
            printf("--------------------------------------------------------------\n");
            printf(ANSI_COLOR_YELLOW "%-10d%-20s%-20s\n" ANSI_COLOR_RESET, (s.week / 2), s.red_teamname, s.blue_teamname);
            printf("-------------------------------------\n");
            temp = 1;
        }
        else if (strcmp(s.red_teamname, name) == 0)
        {
            printf("\n\n--------------------------------------------------------------");
            printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-20s\n" ANSI_COLOR_RESET, "week", "red_team", "blue_team");
            printf("--------------------------------------------------------------\n");
            printf(ANSI_COLOR_YELLOW "%-10d%-20s%-20s\n" ANSI_COLOR_RESET, (s.week / 2), s.red_teamname, s.blue_teamname);
            printf("-------------------------------------\n");
            temp = 1;
        }
    }
    if (temp == 0)
    {
        printf(ANSI_COLOR_RED "\n\aERROR: ** Unfortunately, you do not participate in the league. **\n" ANSI_COLOR_RESET);
    }
    Coahcpage(name);
}
void Upcoming_Opponent(char *name)
{
    twl tw;
    FILE *fpt = fopen("league.txt", "r");
    int week;
    int count = 0;
    char status[10];
    int temp = 0;
    while (fread(&tw, sizeof(tw), 1, fpt))
    {
        week = tw.entery;
        strcpy(status, tw.status);
    }
    fclose(fpt);
    sms s;
    FILE *fplm = fopen("league_matches.txt", "r");
    while (fread(&s, sizeof(sms), 1, fplm) && count < 2)
    {
        if (s.week <= week)
        {
            if (strcmp(s.blue_teamname, name) == 0)
            {
                show_players_of_team_for_match(s.red_teamname);
                printf("\nTotal attack power of team '%s' = %d\n", s.red_team_atck, s.blue_teamname);
                printf("\nTotal defensive power of team '%s' = %d\n", s.red_team_defense, s.red_teamname);
                temp = 1;
                Coahcpage(name);
            }
            else if (strcmp(s.red_teamname, name) == 0)
            {
                show_players_of_team_for_match(s.blue_teamname);
                printf("\nTotal attack power of team '%s' = %d\n", s.blue_team_atck, s.blue_teamname);
                printf("\nTotal defensive power of team '%s' = %d\n", s.blue_team_defence, s.blue_teamname);
                temp = 1;
                Coahcpage(name);
            }
            count++;
        }
    }
    if (count == 1, temp == 0)
    {
        printf(ANSI_COLOR_RED "\nERROR: ** Unfortunately, you do not participate in the league. **\n" ANSI_COLOR_RESET);
    }
    Coahcpage(name);
}
void Change_password() // pass
{
    printf("\n");
    char coachmail[Max];
    char password[Max];
    printf(ANSI_COLOR_CYAN "Enter the mail of coach :\n" ANSI_COLOR_RESET);

    scanf("%s", &coachmail);
    printf(ANSI_COLOR_CYAN "Enter your password :\n" ANSI_COLOR_RESET);
    scanf("%s", &password);
    if (namepass_check_update_change(coachmail, password))
    {
        namepass_update_change(coachmail);
    }
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match password. **\n\n\a" ANSI_COLOR_RESET);
    }

    enter1();
    return;
}
void sort_by_points()
{
    stp *s, s1;
    FILE *fp;
    fp = fopen("team_info.txt", "r");
    fseek(fp, 0, SEEK_END);
    int n = ftell(fp) / sizeof(stp);
    s = (stp *)calloc(n, sizeof(stp));

    rewind(fp);
    for (int i = 0; i < n; i++)
    {
        fread(&s[i], sizeof(stp), 1, fp);
    }
    fclose(fp);
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (s[i].points < s[j].points)
            {
                s1 = s[i];
                s[i] = s[j];
                s[j] = s1;
            }
            else if (s[i].points == s[j].points)
            {
                if (s[i].gd < s[j].gd)
                {
                    s1 = s[i];
                    s[i] = s[j];
                    s[j] = s1;
                }
            }
        }
    }

    fp = fopen("team_info.txt", "w");
    for (int i = 0; i < n; i++)
    {

        fwrite(&s[i], sizeof(stp), 1, fp);
    }
    fclose(fp);
    printf("\n");
}

// Teams Functions
int ID_check_team(int id)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == id)
        {
            allocated = 1;
            break;
        }
    }
    if (allocated == 0)
        return id;
    else
    {
        srand(time(0));
        return ID_check_team((rand() % (upper - lower + 1)) + lower);
    }

    fclose(fp);
}
int name_check_team(char *name)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            allocated = 1;
        }
    }
    if (allocated == 0)
        return 1;
    else
    {
        printf_red1("\n\aThe name has been taken before choose another name please\n");
        return 0;
    }

    fclose(fp);
}

// Players Functions
int ID_check_player(int id)
{
    FILE *fp = fopen("player_info.txt", "r");
    player p1;
    int allocated = 0;
    while (fread(&p1, sizeof(player), 1, fp))
    {
        if (p1.ID == id)
        {
            allocated = 1;
            break;
        }
    }
    if (allocated == 0)
        return id;
    else
        return ID_check_player((rand() % (upper1 - lower1 + 1)) + lower1);

    fclose(fp);
}

// Check Functions
int namepass_check_signin(char *name, char *pass)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            if (strcmp(tp.password, pass) == 0)
            {
                printf_blue1("\nYou're welcome coach!\n\a");
                allocated = 1;
                break;
            }
        }
    }
    if (allocated == 1)
        return 1;
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match password. **\n\n\a" ANSI_COLOR_RESET);
        enter1();
    }

    fclose(fp);
}
int namepass_check_update(char *name, char *pass)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            if (strcmp(tp.password, pass) == 0)
            {
                allocated = 1;
                break;
            }
        }
    }
    if (allocated == 1)
        return 1;
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match password. **\n\n\a" ANSI_COLOR_RESET);
        Coahcpage(name);
    }

    fclose(fp);
}
int namepass_check_update_forgot(char *name, char *pass)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            if (strcmp(tp.coachmail, pass) == 0)
            {
                printf_blue1("\nYou can change your password now!\n\n\a");
                allocated = 1;
                break;
            }
        }
    }
    if (allocated == 1)
        return 1;
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match password. **\n\n\a" ANSI_COLOR_RESET);
        enter1();
    }

    fclose(fp);
}
int namepass_check_update_change(char *coachmail, char *pass)
{
    FILE *fp = fopen("team_info.txt", "r");
    stp tp;
    int allocated = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.coachmail, coachmail) == 0)
        {
            if (strcmp(tp.password, pass) == 0)
            {
                printf_blue1("\nYou can change your password now!\n\n\a");
                allocated = 1;
                break;
            }
        }
    }
    if (allocated == 1)
        return 1;
    else
    {
        printf(ANSI_COLOR_RED "\n** Error : Username does not match password. **\n\n\a" ANSI_COLOR_RESET);
        enter1();
    }

    fclose(fp);
}

// Update Functions
void namepass_update(char *name)
{
    stp tp;
    FILE *fp, *fp1;
    int found = 0;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            found = 1;
            char pass[50];
            printf(ANSI_COLOR_CYAN "Enter new password : " ANSI_COLOR_RESET);
            scanf("%s", pass);
            strcpy(tp.password, pass);
        }

        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    if (namepass_check_update(tp.name, tp.password))
        printf(ANSI_COLOR_BLUE "\nYour password has been successfully updated.\n" ANSI_COLOR_RESET);
    else
        printf(ANSI_COLOR_RED "\nSorry, your password could not be updated.\n" ANSI_COLOR_RESET);
    printf("\n");
}
void namepass_update_change(char *coachmail)
{
    stp tp;
    FILE *fp, *fp1;
    int found = 0;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.coachmail, coachmail) == 0)
        {
            found = 1;
            char pass[50];
            printf(ANSI_COLOR_CYAN "Enter new password : " ANSI_COLOR_RESET);
            scanf("%s", pass);
            strcpy(tp.password, pass);
        }

        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    if (namepass_check_update(tp.name, tp.password))
        printf(ANSI_COLOR_BLUE "\nYour password has been successfully updated.\n" ANSI_COLOR_RESET);
    else
        printf(ANSI_COLOR_RED "\nSorry, your password could not be updated.\n" ANSI_COLOR_RESET);
    printf("\n");
}
int Show_players_for_buy(char *name) // pass
{
    player p1;
    FILE *fp;
    int flag = 0;

    fp = fopen("players_info.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-30s%-30s%-20s%-10s", "ID", "Name", "Atacking_power", "Defencing_power", "Status", "Value" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-20s%-30s%-30s%-20s%-10s", "--", "----", "--------------", "---------------", "------", "-----" ANSI_COLOR_RESET);

    while (fread(&p1, sizeof(player), 1, fp))
    {
        if (strcmp(p1.status, "Free Agent") == 0)
        {
            printf(ANSI_COLOR_YELLOW "\n%-10d%-20s%-30d%-30d%-20s%-10d" ANSI_COLOR_RESET, p1.ID, p1.name, p1.Atacking_power, p1.Defencing_power, p1.status, p1.value);
            printf_cyan1("\n---------------------------------------------------------------------------------------------------------------------");
            flag = 1;
        }
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of players: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
    return flag;
}
int Show_players_for_sell(char *name) // pass
{
    player p1;
    FILE *fp;
    int flag = 0;
    int count = 0;
    fp = fopen("players_info.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-30s%-30s%-20s%-10s", "ID", "Name", "Atacking_power", "Defencing_power", "Status", "Value" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-20s%-30s%-30s%-20s%-10s", "--", "----", "--------------", "---------------", "------", "-----" ANSI_COLOR_RESET);

    while (fread(&p1, sizeof(player), 1, fp))
    {
        if (strcmp(p1.status, name) == 0)
        {
            printf(ANSI_COLOR_YELLOW "\n%-10d%-20s%-30d%-30d%-20s%-10d" ANSI_COLOR_RESET, p1.ID, p1.name, p1.Atacking_power, p1.Defencing_power, p1.status, p1.value);
            printf_cyan1("\n---------------------------------------------------------------------------------------------------------------------");
            flag = 1;
            count++;
        }
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of players: %d\n" ANSI_COLOR_RESET, count);
    fclose(fp);
    return flag;
}

void Show_Teams_temp() // pass
{
    stp tp;
    FILE *fp;
    fp = fopen("team_info.txt", "r");
    int flag = 0;
    printf(ANSI_COLOR_BLUE "\n%-10s%-30s%-30s%-10s%-10s", "ID", "Name", "Coach-mail", "Money", "points" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-30s%-30s%-10s%-10s", "--", "----", "----------", "-----", "------" ANSI_COLOR_RESET);

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        printf(ANSI_COLOR_YELLOW "\n%-10d%-30s%-30s%-10d%-5d" ANSI_COLOR_RESET, tp.ID, tp.name, tp.coachmail, tp.Money, tp.points);
        flag++;
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of teams: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
}

int show_players_of_team(char *name)
{
    player p1;
    FILE *fp;
    int flag = 0;
    fp = fopen("players_info.txt", "r");
    int count = 0;
    printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-30s%-30s%-20s%-10s", "ID", "Name", "Atacking_power", "Defencing_power", "Status", "Value" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-20s%-30s%-30s%-20s%-10s", "--", "----", "--------------", "---------------", "------", "-----" ANSI_COLOR_RESET);

    while (fread(&p1, sizeof(player), 1, fp))
    {
        if (strcmp(p1.status, name) == 0)
        {
            printf(ANSI_COLOR_YELLOW "\n%-10d%-20s%-30d%-30d%-20s%-10d" ANSI_COLOR_RESET, p1.ID, p1.name, p1.Atacking_power, p1.Defencing_power, p1.status, p1.value);
            printf_cyan1("\n---------------------------------------------------------------------------------------------------------------------");
            flag = 1;
            count++;
        }
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of players: %d\n" ANSI_COLOR_RESET, count);
    fclose(fp);
    return flag;
}

int show_players_of_team_for_match(char *name)
{
    stp tp;
    FILE *fp;
    int flag = 0;
    fp = fopen("matchday.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-30s%-30s%-20s%-10s", "ID", "Name", "Atacking_power", "Defencing_power", "Status", "Value" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-20s%-30s%-30s%-20s%-10s", "--", "----", "--------------", "---------------", "------", "-----" ANSI_COLOR_RESET);

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (strcmp(tp.name, name) == 0)
        {
            for (int i = 0; i < 5; i++)
            {
                printf(ANSI_COLOR_YELLOW "\n%-10d%-20s%-30d%-30d%-20s%-10d" ANSI_COLOR_RESET, tp.mplayer[i].m_ID, tp.mplayer[i].m_name, tp.mplayer[i].m_Atacking_power, tp.mplayer[i].m_defencing_power, tp.mplayer[i].m_STATUS, tp.mplayer[i].m_value);
                printf_cyan1("\n---------------------------------------------------------------------------------------------------------------------");
                flag++;
            }
        }
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of players: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
    return flag;
}
void show_teams_ready() // pass
{

    stp tp;
    FILE *fp;
    int flag = 0;
    fp = fopen("ready_for_match.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-30s%-30s%-10s%-10s", "ID", "Name", "Coach-mail", "Money", "CUPS" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-30s%-30s%-10s%-10s", "--", "----", "----------", "-----", "----" ANSI_COLOR_RESET);

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        printf(ANSI_COLOR_YELLOW "\n%-10d%-30s%-30s%-10d%-5d" ANSI_COLOR_RESET, tp.ID, tp.name, tp.coachmail, tp.Money, tp.CUPS);
        printf("\n------------------------------------------------------------------------------------------");
        flag++;
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of teams: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
}

void start_league()
{
    twl tw;
    int ans = 0;
    FILE *fp = fopen("league.txt", "r");
    while (fread(&tw, sizeof(twl), 1, fp))
    {
        ans = 1;
    }
    fclose(fp);
    if (!ans)
    {
        show_teams_ready();

        int i = 0;
        stp tp;
        sms s;
        int ready = 0;
        int lst_teams[4];
        int temp = 0;
        int rno;
        FILE *fpm = fopen("ready_for_match.txt", "r");
        FILE *fpl = fopen("league_teams.txt", "a");

        fseek(fpm, 0, SEEK_END);
        int n = ftell(fpm) / sizeof(stp);
        rewind(fpm);
        if (n < 4) // = 4
        {
            printf(ANSI_COLOR_RED "\nERROR : ** Too few teams are ready, You can't start league now. **\n" ANSI_COLOR_RESET);
            Central_core();
        }

        FILE *fpt = fopen("league.txt", "w");
        strcpy(tw.status, "Started");
        tw.entery = 1;
        fwrite(&tw, sizeof(twl), 1, fpt);

        while (i < 4) // i= 4
        {
            printf(ANSI_COLOR_CYAN "\nEnter the desired team %d ID: " ANSI_COLOR_RESET, i + 1);
            scanf("%d", &rno);
            for (int k = 0; k < 4; k++) // k = 4
            {
                if (rno == lst_teams[k])
                {
                    temp = 1;
                }
            }
            if (!temp)
            {
                while (fread(&tp, sizeof(stp), 1, fpm))
                {
                    if (rno == tp.ID)
                    {
                        fwrite(&tp, sizeof(stp), 1, fpl);
                        lst_teams[i] = tp.ID;
                        i++;
                        fseek(fpm, 0, SEEK_SET);
                        break;
                    }
                }
            }
            if (temp == 1)
            {
                printf(ANSI_COLOR_RED "ERROR : ** You have already selected this team. **\n" ANSI_COLOR_RESET);
                temp = 0;
            }
        }
        fclose(fpm);
        fclose(fpl);
        int index1, index2;
        FILE *fplt = fopen("matchday.txt", "r");
        FILE *fplm = fopen("league_matches.txt", "w");
        int temp1 = 0, temp2 = 0;
        if (show_teams_for_league() == 4) // = 4
        {
            srand(time(0));
            for (int hafteh = 0; hafteh < 6; hafteh++)
            {
                if (hafteh != 0)
                {
                    fseek(fplt, 0, SEEK_SET);
                    temp1 = 0;
                    temp2 = 0;
                }
                do
                {
                    index1 = ((rand() % (second - first + 1)));
                    index2 = ((rand() % (second - first + 1)));
                } while (index1 == index2);
                s.blue_team_ID = lst_teams[index1];
                s.red_team_ID = lst_teams[index2];
                s.blue_team_atck = 0;
                s.blue_team_defence = 0;
                s.red_team_atck = 0;
                s.red_team_defense = 0;
                while (fread(&tp, sizeof(stp), 1, fplt))
                {
                    if (tp.ID == s.blue_team_ID)
                    {
                        strcpy(s.blue_teamname, tp.name);
                        for (int i = 0; i < 5; i++)
                        {
                            s.blue_team_atck += tp.mplayer[i].m_Atacking_power;
                            s.blue_team_defence += tp.mplayer[i].m_defencing_power;
                            fseek(fplt, 0, SEEK_SET);
                            temp1 = 1;
                        }
                    }
                    else if (tp.ID == s.red_team_ID)
                    {
                        strcpy(s.red_teamname, tp.name);
                        for (int i = 0; i < 5; i++)
                        {
                            s.red_team_atck += tp.mplayer[i].m_Atacking_power;
                            s.red_team_defense += tp.mplayer[i].m_defencing_power;
                            fseek(fplt, 0, SEEK_SET);
                            temp2 = 1;
                        }
                    }
                    if (temp1 == temp2)
                    {
                        s.blue_team_goals = (s.blue_team_atck - s.red_team_defense) / 100;
                        s.red_team_goals = (s.red_team_atck - s.blue_team_defence) / 100;
                        s.week = hafteh;
                        printf("\n\n--------------------------------------------------------------");
                        printf(ANSI_COLOR_BLUE "\n%-10s%-20s%-20s\n" ANSI_COLOR_RESET, "week", "red_team", "blue_team");
                        printf("--------------------------------------------------------------\n");
                        printf(ANSI_COLOR_YELLOW "%-10d%-20s%-20s\n" ANSI_COLOR_RESET, hafteh + 1, s.red_teamname, s.blue_teamname);
                        printf("-------------------------------------\n");
                        fwrite(&s, sizeof(sms), 1, fplm);
                    }
                }
            }
        }
        fclose(fplm);
        fclose(fplt);
        fclose(fpt);
    }
    else
    {
        printf(ANSI_COLOR_RED "\nERROR: ** The league is being held **\n" ANSI_COLOR_RESET);
    }
    Central_core();
}
int show_teams_for_league()
{
    stp tp;
    FILE *fp;
    int rno;
    int flag = 0;
    fp = fopen("league_teams.txt", "r");
    printf(ANSI_COLOR_BLUE "\n%-10s%-30s%-30s%-10s%-10s", "ID", "Name", "Coach-mail", "Money", "CUPS" ANSI_COLOR_RESET);
    printf(ANSI_COLOR_CYAN "\n%-10s%-30s%-30s%-10s%-10s", "--", "----", "----------", "-----", "----" ANSI_COLOR_RESET);

    while (fread(&tp, sizeof(stp), 1, fp))
    {
        printf(ANSI_COLOR_YELLOW "\n%-10d%-30s%-30s%-10d%-5d" ANSI_COLOR_RESET, tp.ID, tp.name, tp.coachmail, tp.Money, tp.CUPS);
        printf("\n------------------------------------------------------------------------------------------");
        flag++;
        if (flag == 4) // flag = 4
            break;
    }
    printf("\n\n");
    printf(ANSI_COLOR_MAGENTA "Number of teams: %d\n" ANSI_COLOR_RESET, flag);
    fclose(fp);
    return flag;
}
int transfer_window()
{
    FILE *fp = fopen("transfer_window.txt", "r");
    twl t;
    char status[10];
    int entery;
    while (fread(&t, sizeof(twl), 1, fp))
    {
        strcpy(status, t.status);
        entery = t.entery;
    }
    fclose(fp);
    int ans = -1;
    if (check_season() == 0) // season not started
    {
        printf(newblue "\nYou can close the transfer window, if you want -> enter 1 : \n" ANSI_COLOR_RESET);
        scanf("%d", &ans);
        if (ans == 1)
        {
            FILE *fpt = fopen("transfer_window.txt", "w");
            strcpy(t.status, "close");
            fwrite(&t, sizeof(twl), 1, fpt);
            printf(ANSI_COLOR_RED "\nThe transfer window is close now. \n" ANSI_COLOR_RESET);
            fclose(fpt);

            return 0;
        }
    }
    else if (check_season() == 1) // first season end
    {
        if (strcmp(status, "open") == 0)
            strcpy(t.status, "close");
        else
            strcpy(t.status, "open");

        printf(newblue "\nYou can %s the transfer window, if you want  -> enter 1 : \n" ANSI_COLOR_RESET, t.status);
        scanf("%d", &ans);
        if (ans == 1)
        {
            FILE *fpt = fopen("transfer_window.txt", "w");
            if (strcmp(t.status, "open") == 0)
            {
                fwrite(&t, sizeof(twl), 1, fpt);
                printf(ANSI_COLOR_RED "\nThe transfer window is %s now. \n" ANSI_COLOR_RESET, t.status);
                return 1;
            }
            else
            {
                fwrite(&t, sizeof(twl), 1, fp);
                printf(ANSI_COLOR_RED "\nThe transfer window is close now. \n" ANSI_COLOR_RESET);

                return 0;
            }
            fclose(fpt);

            return 1;
        }
    }
    else if (check_season() == 2) // end of second Season
    {
        printf(newblue "\nYou can open the transfer window, if you want -> enter 1 : \n" ANSI_COLOR_RESET);
        scanf("%d", &ans);
        if (ans == 1)
        {
            FILE *fpt = fopen("transfer_window.txt", "w");
            strcpy(t.status, "open");
            fwrite(&t, sizeof(twl), 1, fpt);
            printf(ANSI_COLOR_RED "\nThe transfer window is open now. \n" ANSI_COLOR_RESET);
            fclose(fpt);

            return 1;
        }
    }
    else if (check_season() == 4) //
    {
        printf_red1("\nThe window is open. Start a league first.\n");
        return 1;
    }
    Central_core();
}
void start_week()
{
    twl tw;
    FILE *fpt = fopen("league.txt", "r");
    int week;
    int count = 0;
    int check = 0;
    char status[10];
    while (fread(&tw, sizeof(tw), 1, fpt))
    {
        week = tw.entery;
        strcpy(status, tw.status);
    }
    fclose(fpt);
    sms s;
    FILE *fplm = fopen("league_matches.txt", "r");
    while (fread(&s, sizeof(sms), 1, fplm) && count < 2)
    {
        check = 1;
        if (count == 1)
        {
            tw.entery += 2;
            strcpy(tw.status, status);
            FILE *fp1 = fopen("league.txt", "w");
            fwrite(&tw, sizeof(tw), 1, fp1);
            fclose(fp1);
        }
        if (s.week <= week)
        {
            printf(ANSI_COLOR_MAGENTA "\t\t\t\nResults of the week %d of the games\n" ANSI_COLOR_RESET, week);
            printf(ANSI_COLOR_YELLOW "\n%-20s%-18s%-20s\n" ANSI_COLOR_RESET, "red_team", "VS", "blue_team");
            fseek(fplm, 0, SEEK_SET);

            printf(ANSI_COLOR_BLUE "%-20s: %-4d VS %-4d :%-20s" ANSI_COLOR_RESET, s.red_teamname, s.red_team_goals, s.blue_team_goals, s.blue_teamname);
            update_powers(s.blue_team_ID);
            update_powers(s.red_team_ID);
            if (s.blue_team_goals > s.red_team_goals)
            {
                update_winner(s.blue_team_ID);
                update_loser(s.red_team_ID);
            }
            else if (s.blue_team_goals < s.red_team_goals)
            {
                update_loser(s.blue_team_ID);
                update_winner(s.red_team_ID);
            }
            else
            {
                update_draw(s.blue_team_ID);
                update_draw(s.blue_team_ID);
            }
            break;
            count++;
        }
    }
    if (!check)
    {
        printf_red1("\nERROR: ** The league has not started yet. **\n");
        adminpage();
    }
}
void end_season()
{
    stp tp;
    int rno;
    FILE *fpt = fopen("team_info.txt", "r");
    League_Standing_forend();
    while (fread(&tp, sizeof(stp), 1, fpt))
    {
        rno = tp.ID;
        fclose(fpt);
        break;
    }
    update_cup(rno);
    League_Standing_forend();

    FILE *fpdt = fopen("data_team.txt", "r");
    FILE *fp21 = fopen("players_info.txt", "w");
    while (fread(&tp, sizeof(stp), 1, fpdt))
    {
        fwrite(&tp, sizeof(stp), 1, fp21);
    }
    fclose(fpdt);
    fclose(fp21);

    FILE *fpdp = fopen("data_player.txt", "r");
    FILE *fp22 = fopen("players_info.txt", "w");
    while (fread(&tp, sizeof(stp), 1, fpdp))
    {
        fwrite(&tp, sizeof(stp), 1, fp22);
    }
    fclose(fpdp);
    fclose(fp22);

    FILE *fp = fopen("league_matches.txt", "w");
    fclose(fp);

    FILE *fp1 = fopen("league.txt", "w");
    fclose(fp1);

    FILE *fp2 = fopen("transfer_window.txt", "w");
    fclose(fp2);

    FILE *fp3 = fopen("league.txt", "w");
    fclose(fp3);

    FILE *fp4 = fopen("ready_for_match.txt", "w");
    fclose(fp4);

    FILE *fp5 = fopen("matchday.txt", "w");
    fclose(fp5);

    enter1();
}

int check_season()
{
    stp tp;
    stp s;
    FILE *fp;
    int flag = 0, end = 0;
    int ans = 0;
    int a = 0;
    fp = fopen("matchday.txt", "r");
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.played == 3)
        {
            a = 1;
            flag++;
        }
        else if (tp.played == 0)
        {
            a = 1;
            ans++;
        }
        else if (tp.played == 6)
        {
            a = 1;
            end++;
        }
    }
    if (!a)
    {
        return 4;
    }
    if (flag == 4)
    {
        return 1; // first season end
    }
    if (ans == 4)
    {
        return 0; // league not started
    }
    if (end == 4)
    {
        return 2;
    }
    return -1;
}

void update_powers(int rno1)
{
    stp tp;
    FILE *fp, *fp1;
    fp = fopen("matchday.txt", "r");
    fp1 = fopen("temp.txt", "w");
    int found = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;
            for (int j = 0; j < 5; j++)
            {
                tp.mplayer[j].m_Atacking_power -= 5;
                tp.mplayer[j].m_defencing_power -= 5;
            }
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("matchday.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n\aERROR : ** Record Not Found **");
    printf("\n");
    start_week();
}

void update_winner(int rno1)
{
    stp tp;
    FILE *fp, *fp1;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");
    int found = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;
            tp.points += 3;
            tp.Money += 5;
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n\aERROR : ** Record Not Found **");
    printf("\n");
}

void update_loser(int rno1)
{
    stp tp;
    FILE *fp, *fp1;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");
    int found = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;
            tp.Money += 1;
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n\aERROR : ** Record Not Found **");
    printf("\n");
}

void update_draw(int rno1)
{
    stp tp;
    FILE *fp, *fp1;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");
    int found = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;
            tp.points += 1;
            tp.Money += 3;
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n\aERROR : ** Record Not Found **");
    printf("\n");
}

void League_Standing_forend() // pass
{
    sort_by_points();
    stp tp;
    FILE *fp = fopen("team_info.txt", "r");
    int rows = 1, columns;
    printf_red1("\n\t\t\tThis is the league table standing.\n\n\a");

    printf_cyan1("    Name\tPlayed\t  Won\tDrawn\tLost\tGF\tGD\tGA\tPoints\n");
    printf("    ----\t------\t  ---\t-----\t---\t--\t--\t--\t------\n\n");
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        switch (rows)
        {
        case 1:
            printf(BHGRN "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 2:
            printf(ANSI_COLOR_GREEN "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 3:
            printf(ANSI_COLOR_YELLOW "%d : " ANSI_COLOR_RESET, rows);
            break;
        case 4:
            printf(ANSI_COLOR_RED "%d : " ANSI_COLOR_RESET, rows);
            break;
        default:
            printf(newblue "%d : " ANSI_COLOR_RESET, rows);
            break;
        }
        while (rows < 5)
        {
            for (columns = 1; columns < 10; columns++)
            {

                switch (columns)
                {
                case 1:
                    printf(ANSI_COLOR_BLUE "%-10s\t" ANSI_COLOR_RESET, tp.name);
                    break;
                case 2:
                    printf("  %d\t  ", tp.played);
                    break;
                case 3:
                    printf("%d\t", tp.won);
                    break;
                case 4:
                    printf(" %d\t", tp.drawn);
                    break;
                case 5:
                    printf("%d\t", tp.lost);
                    break;
                case 6:
                    printf("%d\t", tp.gf);
                    break;
                case 7:
                    printf("%d\t", tp.gd);
                    break;
                case 8:
                    printf("%d\t", tp.ga);
                    break;
                case 9:
                    printf(ANSI_COLOR_RED "  %d\t\n" ANSI_COLOR_RESET, tp.points);
                    break;
                }
            }

            printf("\n|-------------------------------------------------------------------------------|\n");
            printf("\n");
            rows++;
            break;
        }
    }
}

void update_cup(int rno1)
{
    stp tp;
    FILE *fp, *fp1;
    fp = fopen("team_info.txt", "r");
    fp1 = fopen("temp.txt", "w");
    int found = 0;
    while (fread(&tp, sizeof(stp), 1, fp))
    {
        if (tp.ID == rno1)
        {
            found = 1;
            tp.CUPS += 1;
        }
        fwrite(&tp, sizeof(stp), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found)
    {
        fp1 = fopen("temp.txt", "r");
        fp = fopen("team_info.txt", "w");
        while (fread(&tp, sizeof(stp), 1, fp1))
        {
            fwrite(&tp, sizeof(stp), 1, fp);
        }

        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n\aERROR : ** Record Not Found **");
    printf("\n");
}