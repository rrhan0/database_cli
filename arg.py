import click
import sys
import mysql.connector
from prettytable import PrettyTable

mysql_client = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    passwd="asdasd",
                                    database="p_info")
mysql_client_cursor = mysql_client.cursor()
table = PrettyTable()
table.field_names = ["ID", "Name", "Email", "Job", "Salary"]


@click.group()
def cli():
    pass


@cli.command("insert")
@click.option('--name', "-n", required=True, help="Name of the person")
@click.option('--email', "-e", required=True, help="Email of the person")
@click.option('--job', "-j", required=True, help="The person's job")
@click.option('--salary', "-s", type=int, required=True, help="The person's salary")
def insert(name, email, job, salary):
    sql = "INSERT INTO accounts (name, email, job, salary) VALUES (%s, %s, %s, %s)"
    val = (name, email, job, salary)
    mysql_client_cursor.execute(sql, val)
    mysql_client.commit()


@cli.command("list")
def show_list():
    mysql_client_cursor.execute("SELECT * FROM accounts")
    table_row = mysql_client_cursor.fetchall()
    for x in table_row:
        table.add_row(x)
    print(table)
    table.clear_rows()


@cli.command("get")
@click.option('--id', "item_id", required=True, help="The ID of the row")
def get_one(item_id):
    mysql_client_cursor.execute("SELECT * FROM accounts WHERE id = " + item_id)
    table_row = mysql_client_cursor.fetchall()
    for x in table_row:
        table.add_row(x)
    print(table)
    table.clear_rows()


@cli.command("delete")
@click.option('--id', "item_id", required=True, help="The ID of the row")
def delete_one(item_id):
    sql = "DELETE FROM accounts WHERE id = " + item_id
    mysql_client_cursor.execute(sql)
    mysql_client.commit()


if __name__ == "__main__":
    cli()
