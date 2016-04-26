#!/usr/bin/python

import argparse
import sqlite3


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("db_file", help="Viper database file")
    parser.add_argument("old_tag", help="Old tag name")
    parser.add_argument("new_tag", help="New tag name")
    args = parser.parse_args()

    conn = sqlite3.connect(args.db_file)
    cur = conn.cursor()

    find_old_tag = "select * from tag where tag = ?;"
    cur.execute(find_old_tag, (args.old_tag,))
    print "Old tag found, id: %s name: %s" % cur.fetchone()

    update_sql = "update tag set tag = ? where tag = ?;"
    cur.execute(update_sql, (args.new_tag, args.old_tag))
    conn.commit()
    print "Update tag %s with %s" % (args.old_tag, args.new_tag)

    select_sql = "select * from tag where tag = ?;"
    cur.execute(select_sql, (args.new_tag,))
    print "New tag, id: %s name: %s" % cur.fetchone()

    conn.close()
