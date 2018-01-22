# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountMaster(models.Model):
    create_date = models.DateField()
    yearmo = models.IntegerField(blank=True, null=True)
    master_id = models.AutoField(primary_key=True)
    state_license_code = models.CharField(max_length=30, blank=True, null=True)
    dba_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.IntegerField(blank=True, null=True)
    telephone_number = models.CharField(max_length=8, blank=True, null=True)
    cust_license = models.CharField(max_length=100, blank=True, null=True)
    license_type_code = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='license_type_code', blank=True, null=True)
    trade_code = models.ForeignKey('TradeChannel', models.DO_NOTHING, db_column='trade_code', blank=True, null=True)
    license_code = models.ForeignKey('AccountType', models.DO_NOTHING, db_column='license_code', blank=True, null=True)
    food_code = models.ForeignKey('FoodType', models.DO_NOTHING, db_column='food_code', blank=True, null=True)
    chain_indicator = models.CharField(max_length=1, blank=True, null=True)
    chain_code = models.ForeignKey('ChainCode', models.DO_NOTHING, db_column='chain_code', blank=True, null=True)
    demographics = models.CharField(max_length=50, blank=True, null=True)
    delete_yn = models.BooleanField()
    state = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'account_master'


class AccountType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(primary_key=True, max_length=15)
    account_type = models.CharField(db_column='account type', max_length=50)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'account_type'


class ChainCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(primary_key=True, max_length=30)
    chain_name = models.CharField(db_column='chain name', max_length=50)  # Field renamed to remove unsuitable characters.
    chain_license_type_code = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='chain license type code')  # Field renamed to remove unsuitable characters.
    chain_trade_channel_code = models.ForeignKey('TradeChannel', models.DO_NOTHING, db_column='chain_trade_channel_code', blank=True, null=True)
    chain_food_type_code = models.ForeignKey('FoodType', models.DO_NOTHING, db_column='chain_food_type_code', blank=True, null=True)
    chain_account_type_code = models.ForeignKey(AccountType, models.DO_NOTHING, db_column='chain_account_type_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chain_code'


class CodeMatching(models.Model):
    retailer_search_string = models.CharField(primary_key=True, max_length=100)
    premise_code = models.ForeignKey('LicenseType', models.DO_NOTHING, db_column='premise_code', blank=True, null=True)
    trade_code = models.ForeignKey('TradeChannel', models.DO_NOTHING, db_column='trade_code', blank=True, null=True)
    food_code = models.ForeignKey('FoodType', models.DO_NOTHING, db_column='food_code', blank=True, null=True)
    chain_code = models.ForeignKey(ChainCode, models.DO_NOTHING, db_column='chain_code', blank=True, null=True)
    account_type_code = models.ForeignKey(AccountType, models.DO_NOTHING, db_column='account_type_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_matching'


class Depl(models.Model):
    sup = models.ForeignKey('SupMaster', models.DO_NOTHING, db_column='sup', primary_key=True)
    sequence_no = models.CharField(max_length=3, blank=True, null=True)
    record_type = models.CharField(max_length=3, blank=True, null=True)
    distributor = models.ForeignKey('DistMaster', models.DO_NOTHING)
    yearmo = models.IntegerField()
    opening_balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trans_in = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    adjustments = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    retail_sales = models.DecimalField(max_digits=65535, decimal_places=65535)
    wholesale_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    transfers_out = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    on_premise_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    off_premise_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    military_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    transportation_sales = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    on_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    in_bond_inventory = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    item_code = models.CharField(max_length=100)
    item_desc = models.TextField()
    item_size = models.TextField()
    item_proof = models.TextField()
    units_per_case = models.CharField(max_length=105)
    receipts = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'depl'
        unique_together = (('sup', 'distributor', 'yearmo', 'item_code'),)


class DistMaster(models.Model):
    id = models.AutoField(primary_key=True)
    master_dist_id = models.CharField(primary_key=True, max_length=30)
    dist_name = models.CharField(max_length=50)
    dist_state = models.CharField(max_length=3)
    dist_address = models.CharField(max_length=50)
    dist_zip = models.IntegerField()
    dist_filename = models.CharField(max_length=50)
    depl_split_script = models.CharField(max_length=50)
    rad_split_script = models.CharField(max_length=50)
    rad_invc_lvl_split_script = models.CharField(max_length=50)
    cust_split_script = models.CharField(max_length=50)
    salesman_split_script = models.CharField(max_length=50)
    prod_update = models.CharField(max_length=50)
    yyyymm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dist_master'


class DistSupCrossreference(models.Model):
    master_dist_id = models.CharField(primary_key=True, max_length=100)
    dist_sup_id = models.CharField(max_length=100)
    master_sup_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dist_sup_crossreference'
        unique_together = (('master_dist_id', 'dist_sup_id'),)


class FoodType(models.Model):
    code = models.CharField(primary_key=True, max_length=30)
    food_type_desc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_type'


class LicenseType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(primary_key=True, max_length=1)
    license_type = models.CharField(db_column='license type', max_length=30)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'license_type'


class Rad(models.Model):
    sup = models.ForeignKey('SupMaster', models.DO_NOTHING, db_column='sup', primary_key=True)
    sequence_no = models.CharField(max_length=3, blank=True, null=True)
    record_type = models.CharField(max_length=3, blank=True, null=True)
    distributor = models.ForeignKey('Sman', models.DO_NOTHING)
    yearmo = models.IntegerField()
    item_code = models.DecimalField(db_column='item code', max_digits=65535, decimal_places=65535)  # Field renamed to remove unsuitable characters.
    case_quantity = models.DecimalField(db_column='case quantity', max_digits=65535, decimal_places=65535)  # Field renamed to remove unsuitable characters.
    dollar_amount = models.DecimalField(db_column='dollar amount', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sales_division = models.CharField(db_column='sales division', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    salesman_number = models.CharField(db_column='salesman number', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_date = models.DateField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    customer_code = models.CharField(db_column='customer code', max_length=100)  # Field renamed to remove unsuitable characters.
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rad'
        unique_together = (('sup', 'distributor', 'yearmo', 'item_code', 'customer_code'),)


class RadInvc(models.Model):
    sup = models.ForeignKey('SupMaster', models.DO_NOTHING, db_column='sup', primary_key=True)
    distributor = models.ForeignKey(DistMaster, models.DO_NOTHING)
    yyyymmdd = models.IntegerField()
    item_code = models.DecimalField(db_column='item code', max_digits=65535, decimal_places=65535)  # Field renamed to remove unsuitable characters.
    case_quantity = models.DecimalField(db_column='case quantity', max_digits=65535, decimal_places=65535)  # Field renamed to remove unsuitable characters.
    dollar_amount = models.DecimalField(db_column='dollar amount', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sales_division = models.CharField(db_column='sales division', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    salesman_number = models.CharField(db_column='salesman number', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_date = models.DateField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rad_invc'
        unique_together = (('sup', 'distributor', 'yyyymmdd', 'item_code'),)


class RetailerXref(models.Model):
    sequence_no = models.IntegerField(blank=True, null=True)
    record_type = models.IntegerField(blank=True, null=True)
    distributor_id = models.CharField(max_length=100)
    create_date = models.DateField()
    yearmo = models.IntegerField(blank=True, null=True)
    wholesaler_customer_code = models.CharField(primary_key=True, max_length=100)
    state_license_code = models.CharField(max_length=30, blank=True, null=True)
    dba_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=3)
    zipcode = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.IntegerField(blank=True, null=True)
    telephone_number = models.CharField(max_length=8, blank=True, null=True)
    license_type = models.CharField(max_length=100, blank=True, null=True)
    chain_indicator = models.CharField(max_length=1, blank=True, null=True)
    chain_code = models.CharField(max_length=10, blank=True, null=True)
    demographics = models.CharField(max_length=50, blank=True, null=True)
    master = models.ForeignKey(AccountMaster, models.DO_NOTHING, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'retailer_xref'
        unique_together = (('wholesaler_customer_code', 'distributor_id'),)


class Sman(models.Model):
    sequence_no = models.CharField(max_length=3, blank=True, null=True)
    record_type = models.CharField(max_length=3, blank=True, null=True)
    distributor_id = models.CharField(primary_key=True, max_length=100)
    create_date = models.IntegerField()
    yearmo = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=30)
    salesman_id = models.CharField(max_length=30)
    salesman_name = models.CharField(max_length=30, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sman'
        unique_together = (('distributor_id', 'salesman_id', 'team'),)


class States(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'states'


class SupData(models.Model):
    sup_id = models.CharField(primary_key=True, max_length=50)
    dist_id = models.CharField(max_length=50)
    city = models.CharField(max_length=100, blank=True, null=True)
    dist_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    prod_id = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=150, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=15, blank=True, null=True)
    pack = models.CharField(max_length=15, blank=True, null=True)
    proof = models.CharField(max_length=15, blank=True, null=True)
    vintage = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField()
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup_data'
        unique_together = (('sup_id', 'dist_id', 'date', 'prod_id'),)
# Unable to inspect table 'sup_incoming_files'
# The error was: permission denied for relation sup_incoming_files



class SupMaster(models.Model):
    id = models.AutoField(primary_key=True)
    master_sup_id = models.CharField(primary_key=True, max_length=30)
    supplier_name = models.CharField(max_length=50)
    supplier_state = models.ForeignKey(States, models.DO_NOTHING, db_column='supplier_state')
    supplier_zip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sup_master'


class TradeChannel(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(primary_key=True, max_length=5)
    trade_channel = models.CharField(db_column='Trade Channel', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'trade_channel'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    sup_dist = models.TextField()  # This field type is a guess.
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'users'


class Zipcode(models.Model):
    zip = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    primary_city = models.CharField(max_length=100)
    acceptable_cities = models.CharField(max_length=300, blank=True, null=True)
    unacceptable_cities = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=4)
    county = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    area_codes = models.IntegerField(blank=True, null=True)
    lattitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    world_region = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    decommisioned = models.CharField(max_length=100, blank=True, null=True)
    estimated_population = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zipcode'
