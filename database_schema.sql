BEGIN;
--
-- Create model Admins
--
CREATE TABLE "admins" ("id" uuid NOT NULL PRIMARY KEY, "full_name" text NOT NULL, "email" text NOT NULL UNIQUE, "phone" varchar(20) NULL, "role" text NOT NULL, "password_hash" text NOT NULL, "is_verified" boolean NULL, "is_blocked" boolean NULL, "failed_login_attempts" integer NULL, "created_at" timestamp with time zone NULL);
--
-- Create model LoanProducts
--
CREATE TABLE "loan_products" ("id" uuid NOT NULL PRIMARY KEY, "name" text NOT NULL, "min_amount" numeric(12, 2) NOT NULL, "max_amount" numeric(12, 2) NOT NULL, "interest_rate" numeric(5, 2) NOT NULL, "duration_months" integer NOT NULL, "created_at" timestamp with time zone NULL);
--
-- Create model Users
--
CREATE TABLE "users" ("id" uuid NOT NULL PRIMARY KEY, "full_name" text NOT NULL, "phone" varchar(20) NOT NULL UNIQUE, "email" text NULL, "is_verified" boolean NULL, "created_at" timestamp with time zone NULL, "updated_at" timestamp with time zone NULL);
--
-- Create model AuditLogs
--
CREATE TABLE "audit_logs" ("id" uuid NOT NULL PRIMARY KEY, "action" text NOT NULL, "table_name" text NOT NULL, "record_id" uuid NULL, "old_data" jsonb NULL, "new_data" jsonb NULL, "created_at" timestamp with time zone NULL, "admin_id" uuid NULL);
--
-- Create model Loans
--
CREATE TABLE "loans" ("id" uuid NOT NULL PRIMARY KEY, "principal_amount" numeric(12, 2) NOT NULL, "interest_rate" numeric(5, 2) NOT NULL, "duration_months" integer NOT NULL, "status" text NULL, "created_at" timestamp with time zone NULL, "loan_product_id" uuid NOT NULL, "user_id" uuid NOT NULL);
--
-- Create model Repayments
--
CREATE TABLE "repayments" ("id" uuid NOT NULL PRIMARY KEY, "amount_paid" numeric(12, 2) NOT NULL, "payment_method" text NULL, "payment_date" timestamp with time zone NULL, "reference_code" text NULL UNIQUE, "loan_id" uuid NOT NULL);
--
-- Create model RepaymentSchedule
--
CREATE TABLE "repayment_schedule" ("id" uuid NOT NULL PRIMARY KEY, "installment_number" integer NOT NULL, "due_date" date NOT NULL, "amount_due" numeric(12, 2) NOT NULL, "is_paid" boolean NULL, "loan_id" uuid NOT NULL);
--
-- Create model UserProfiles
--
CREATE TABLE "user_profiles" ("id" uuid NOT NULL PRIMARY KEY, "national_id" varchar(50) NULL UNIQUE, "date_of_birth" date NULL, "address" text NULL, "employment_status" text NULL, "monthly_income" numeric(12, 2) NULL, "created_at" timestamp with time zone NULL, "user_id" uuid NOT NULL UNIQUE);
--
-- Create model Transactions
--
CREATE TABLE "transactions" ("id" uuid NOT NULL PRIMARY KEY, "type" text NOT NULL, "amount" numeric(12, 2) NOT NULL, "created_at" timestamp with time zone NULL, "user_id" uuid NOT NULL);
--
-- Create model Notifications
--
CREATE TABLE "notifications" ("id" uuid NOT NULL PRIMARY KEY, "message" text NOT NULL, "is_read" boolean NULL, "created_at" timestamp with time zone NULL, "user_id" uuid NOT NULL);
CREATE INDEX "admins_email_bb3581a9_like" ON "admins" ("email" text_pattern_ops);
CREATE INDEX "users_phone_2b77170a_like" ON "users" ("phone" varchar_pattern_ops);
ALTER TABLE "audit_logs" ADD CONSTRAINT "audit_logs_admin_id_f6e71a2f_fk_admins_id" FOREIGN KEY ("admin_id") REFERENCES "admins" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "audit_logs_admin_id_f6e71a2f" ON "audit_logs" ("admin_id");
ALTER TABLE "loans" ADD CONSTRAINT "loans_loan_product_id_5460cca4_fk_loan_products_id" FOREIGN KEY ("loan_product_id") REFERENCES "loan_products" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "loans" ADD CONSTRAINT "loans_user_id_e6467baa_fk_users_id" FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "loans_loan_product_id_5460cca4" ON "loans" ("loan_product_id");
CREATE INDEX "loans_user_id_e6467baa" ON "loans" ("user_id");
ALTER TABLE "repayments" ADD CONSTRAINT "repayments_loan_id_58f9f13b_fk_loans_id" FOREIGN KEY ("loan_id") REFERENCES "loans" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "repayments_reference_code_53c76468_like" ON "repayments" ("reference_code" text_pattern_ops);
CREATE INDEX "repayments_loan_id_58f9f13b" ON "repayments" ("loan_id");
ALTER TABLE "repayment_schedule" ADD CONSTRAINT "repayment_schedule_loan_id_326a95e3_fk_loans_id" FOREIGN KEY ("loan_id") REFERENCES "loans" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "repayment_schedule_loan_id_326a95e3" ON "repayment_schedule" ("loan_id");
ALTER TABLE "user_profiles" ADD CONSTRAINT "user_profiles_user_id_8c5ab5fe_fk_users_id" FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "user_profiles_national_id_4d3cc9a2_like" ON "user_profiles" ("national_id" varchar_pattern_ops);
ALTER TABLE "transactions" ADD CONSTRAINT "transactions_user_id_766cc893_fk_users_id" FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "transactions_user_id_766cc893" ON "transactions" ("user_id");
ALTER TABLE "notifications" ADD CONSTRAINT "notifications_user_id_468e288d_fk_users_id" FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "notifications_user_id_468e288d" ON "notifications" ("user_id");
COMMIT;
