



create database arknights;
use arknights;

create table skill_info(
    skill_name varchar(20) not null primary key,
    skill_level integer not null,
    skill_description varchar(100) not null,
    skill_effect varchar(100) not null
);

create table skin_info(
    skin_name varchar(20) not null primary key,
    skin_printer varchar(20) not null,
    skin_description varchar(200) not null,
    skin_whe_buy boolean not null,
    skin_can_buy boolean not null,
    skin_prict integer not null,
    skin_wear boolean not null
);

create table voice_info(
    voice_no varchar(20) not null primary key,
    voice_language varchar(20) not null,
    voice_actor varchar(20) not null,
    voice_description varchar(20) not null,
    voice_content varchar(200) not null,
    voice_whe_unlock boolean not null,
    voice_unlock_condition varchar(100) not null
);

create table module_info(
    module_name varchar(20) not null primary key,
    unlock_condition varchar(100) not null,
    attribute_update varchar(100) not null,
    characteristic_update varchar(100) not null
);

create table details_info(
    details_no varchar(20) not null primary key,
    details_skin varchar(20) not null,
    details_voice varchar(20) not null,
    details_archives varchar(2000) not null,
    details_plot varchar(20) not null,
    details_map varchar(20) not null,
    constraint `skin_con` foreign key (`details_skin`)
        references `skin_info`(`skin_name`),
    constraint `voice_con` foreign key (`details_voice`)
        references `voice_info`(`voice_no`)
);

create table operator_attribute_info(
    attribute_no varchar(20) not null primary key,
    level integer not null,
    exp integer not null,
    potential integer not null,
    promotion integer not null,
    skill varchar(20) not null,
    HP integer not null,
    attack integer not null,
    attack_mode varchar(20) not null,
    attack_speed integer not null,
    physical_defense integer not null,
    magic_defense integer not null,
    cost integer not null,
    return_time integer not null,
    constraint `skill_con` foreign key (`skill`)
        references `skill_info`(`skill_name`)
);

create table operator_base_info(
    no varchar(10) not null primary key,
    name varchar(20) not null,
    occupation varchar(20) not null,
    rarity integer not null,
    position varchar(20) not null,
    gender varchar(20) not null,
    tag varchar(20) not null,
    characteristic varchar(20) not null,
    module varchar(20) not null,
    attribute varchar(20) not null,
    details varchar(20) not null,
    constraint `module_con` foreign key (`module`)
        references `module_info`(`module_name`),
    constraint `attribute_con` foreign key (`attribute`)
        references `operator_attribute_info`(`attribute_no`),
    constraint `details_con` foreign key (`details`)
        references `details_info`(`details_no`)
);

create table user_info(
    ID varchar(10) not null primary key,
    password varchar(20) not null,
    name varchar(20) not null,
    operator_total_num integer not null,
    supporter varchar(10) not null,
    assistant varchar(10) not null,
    constraint `supporter_con` foreign key (`supporter`)
        references `operator_base_info`(`no`),
    constraint `assistant_con` foreign key (`assistant`)
        references `operator_base_info`(`no`)
);
