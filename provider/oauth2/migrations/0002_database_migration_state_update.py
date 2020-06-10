# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-10 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import provider.utils


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=migrations.RunSQL.noop,
            state_operations=[
                migrations.AlterField(
                    model_name='accesstoken',
                    name='expires',
                    field=models.DateTimeField(default=provider.utils.get_token_expiry),
                ),
                migrations.AlterField(
                    model_name='accesstoken',
                    name='scope',
                    field=models.IntegerField(choices=[(2, 'read'), (4, 'write'), (6, 'read+write')], default=2),
                ),
                migrations.AlterField(
                    model_name='accesstoken',
                    name='token',
                    field=models.CharField(default=provider.utils.long_token, max_length=255),
                ),
                migrations.AlterField(
                    model_name='client',
                    name='client_type',
                    field=models.IntegerField(choices=[(0, 'Confidential (Web applications)'), (1, 'Public (Native and JS applications)')]),
                ),
                migrations.AlterField(
                    model_name='client',
                    name='redirect_uri',
                    field=models.URLField(help_text="Your application's callback URL"),
                ),
                migrations.AlterField(
                    model_name='client',
                    name='url',
                    field=models.URLField(help_text="Your application's URL."),
                ),
            ]
        )
    ]


"""
BEGIN;
--
-- Alter field expires on accesstoken
--
ALTER TABLE "oauth2_accesstoken" RENAME TO "oauth2_accesstoken__old";
CREATE TABLE "oauth2_accesstoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "expires" datetime NOT NULL, "token" varchar(255) NOT NULL, "scope" integer NOT NULL, "client_id" integer NOT NULL REFERENCES "oauth2_client" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "oauth2_accesstoken" ("id", "token", "scope", "client_id", "user_id", "expires") SELECT "id", "token", "scope", "client_id", "user_id", "expires" FROM "oauth2_accesstoken__old";
DROP TABLE "oauth2_accesstoken__old";
CREATE INDEX "oauth2_accesstoken_token_24468552" ON "oauth2_accesstoken" ("token");
CREATE INDEX "oauth2_accesstoken_client_id_e5c1beda" ON "oauth2_accesstoken" ("client_id");
CREATE INDEX "oauth2_accesstoken_user_id_bcf4c395" ON "oauth2_accesstoken" ("user_id");
--
-- Alter field scope on accesstoken
--
ALTER TABLE "oauth2_accesstoken" RENAME TO "oauth2_accesstoken__old";
CREATE TABLE "oauth2_accesstoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "token" varchar(255) NOT NULL, "expires" datetime NOT NULL, "client_id" integer NOT NULL REFERENCES "oauth2_client" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "scope" integer NOT NULL);
INSERT INTO "oauth2_accesstoken" ("id", "token", "expires", "client_id", "user_id", "scope") SELECT "id", "token", "expires", "client_id", "user_id", "scope" FROM "oauth2_accesstoken__old";
DROP TABLE "oauth2_accesstoken__old";
CREATE INDEX "oauth2_accesstoken_token_24468552" ON "oauth2_accesstoken" ("token");
CREATE INDEX "oauth2_accesstoken_client_id_e5c1beda" ON "oauth2_accesstoken" ("client_id");
CREATE INDEX "oauth2_accesstoken_user_id_bcf4c395" ON "oauth2_accesstoken" ("user_id");
--
-- Alter field token on accesstoken
--
ALTER TABLE "oauth2_accesstoken" RENAME TO "oauth2_accesstoken__old";
CREATE TABLE "oauth2_accesstoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "expires" datetime NOT NULL, "scope" integer NOT NULL, "client_id" integer NOT NULL REFERENCES "oauth2_client" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "token" varchar(255) NOT NULL);
INSERT INTO "oauth2_accesstoken" ("id", "expires", "scope", "client_id", "user_id", "token") SELECT "id", "expires", "scope", "client_id", "user_id", "token" FROM "oauth2_accesstoken__old";
DROP TABLE "oauth2_accesstoken__old";
CREATE INDEX "oauth2_accesstoken_client_id_e5c1beda" ON "oauth2_accesstoken" ("client_id");
CREATE INDEX "oauth2_accesstoken_user_id_bcf4c395" ON "oauth2_accesstoken" ("user_id");
--
-- Alter field client_type on client
--
ALTER TABLE "oauth2_client" RENAME TO "oauth2_client__old";
CREATE TABLE "oauth2_client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "url" varchar(200) NOT NULL, "redirect_uri" varchar(200) NOT NULL, "client_id" varchar(255) NOT NULL, "client_secret" varchar(255) NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id"), "client_type" integer NOT NULL);
INSERT INTO "oauth2_client" ("id", "name", "url", "redirect_uri", "client_id", "client_secret", "user_id", "client_type") SELECT "id", "name", "url", "redirect_uri", "client_id", "client_secret", "user_id", "client_type" FROM "oauth2_client__old";
DROP TABLE "oauth2_client__old";
CREATE INDEX "oauth2_client_user_id_21c89c78" ON "oauth2_client" ("user_id");
--
-- Alter field redirect_uri on client
--
ALTER TABLE "oauth2_client" RENAME TO "oauth2_client__old";
CREATE TABLE "oauth2_client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "url" varchar(200) NOT NULL, "client_id" varchar(255) NOT NULL, "client_secret" varchar(255) NOT NULL, "client_type" integer NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id"), "redirect_uri" varchar(200) NOT NULL);
INSERT INTO "oauth2_client" ("id", "name", "url", "client_id", "client_secret", "client_type", "user_id", "redirect_uri") SELECT "id", "name", "url", "client_id", "client_secret", "client_type", "user_id", "redirect_uri" FROM "oauth2_client__old";
DROP TABLE "oauth2_client__old";
CREATE INDEX "oauth2_client_user_id_21c89c78" ON "oauth2_client" ("user_id");
--
-- Alter field url on client
--
ALTER TABLE "oauth2_client" RENAME TO "oauth2_client__old";
CREATE TABLE "oauth2_client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "redirect_uri" varchar(200) NOT NULL, "client_id" varchar(255) NOT NULL, "client_secret" varchar(255) NOT NULL, "client_type" integer NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id"), "url" varchar(200) NOT NULL);
INSERT INTO "oauth2_client" ("id", "name", "redirect_uri", "client_id", "client_secret", "client_type", "user_id", "url") SELECT "id", "name", "redirect_uri", "client_id", "client_secret", "client_type", "user_id", "url" FROM "oauth2_client__old";
DROP TABLE "oauth2_client__old";
CREATE INDEX "oauth2_client_user_id_21c89c78" ON "oauth2_client" ("user_id");
COMMIT;
"""
