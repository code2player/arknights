



create database arknights;
use arknights;



create table skin_info(
    skin_name varchar(20) not null primary key,
    skin_operator_name varchar(20) not null,
    skin_printer varchar(20) not null,
    skin_description varchar(200) not null,
    skin_can_buy boolean not null,
    skin_price integer not null
);

create table voice_info(
    voice_no varchar(20) not null primary key,
    voice_operator_name varchar(20) not null,
    voice_language varchar(20) not null,
    voice_actor varchar(20) not null,
    voice_description varchar(40) not null,
    voice_content varchar(200) not null
);

create table details_info(
    details_no varchar(20) not null primary key,
    details_operator_name varchar(20) not null,
    details_archives varchar(2000) not null,
    details_plot varchar(400) not null,
    details_map varchar(400) not null
);

create table operator_attribute_info(
    attribute_no varchar(20) not null primary key,
    operator_name varchar(20) not null,
    level integer not null,
    exp integer not null,
    potential integer not null,
    promotion integer not null,
    HP integer not null,
    attack integer not null,
    attack_mode varchar(20) not null,
    attack_speed integer not null,
    physical_defense integer not null,
    magic_defense integer not null,
    cost integer not null,
    return_time integer not null
);

create table operator_base_info(
    name varchar(20) not null primary key,
    no varchar(10) not null,
    occupation varchar(20) not null,
    rarity integer not null,
    position varchar(20) not null,
    gender varchar(20) not null,
    tag varchar(40) not null,
    characteristic varchar(100) not null,
    attribute varchar(20) not null,
    details varchar(20) not null,
    constraint `attribute_con` foreign key (`attribute`)
        references `operator_attribute_info`(`attribute_no`),
    constraint `details_con` foreign key (`details`)
        references `details_info`(`details_no`)
);

create table skill_info(
    skill_name varchar(20) not null primary key,
    operator_name varchar(20) not null,
    skill_level integer not null,
    skill_description varchar(100) not null,
    skill_effect varchar(100) not null,
    constraint `skill_con` foreign key (`operator_name`)
        references `operator_base_info`(`name`)
);

create table user_info(
    ID varchar(10) not null primary key,
    password varchar(20) not null,
    email varchar(50) not null,
    phone varchar(50) not null,
    operator_total_num integer not null,
    supporter varchar(20) not null,
    assistant varchar(20) not null,
    constraint `supporter_con` foreign key (`supporter`)
        references `operator_base_info`(`name`),
    constraint `assistant_con` foreign key (`assistant`)
        references `operator_base_info`(`name`)
);





INSERT INTO `skin_info` VALUES ('精一立绘','能天使', '幻象黑兔','干员平时最常穿着的服装。\n
虽然不一定比制服更实用，但是一定是干员最舒适的搭配之一。',True,0);
INSERT INTO `skin_info` VALUES ('精二立绘','能天使', '幻象黑兔','晋升后，经过调整的服装。\n
根据干员的经验，对服装细节进行改进，针对一些作战环境进行了特化处理。在满足战斗需求的同时，最大程度还原各位干员熟悉的舒适穿着体验。',False,18);


INSERT INTO `voice_info` VALUES ('01','能天使', '中文','蔡书锦','进入游戏1','你好，欢迎回来');
INSERT INTO `voice_info` VALUES ('02','能天使', '日语','石见舞菜香','进入游戏2','早上好');

INSERT INTO `details_info` VALUES ('0143','能天使', '【代号】能天使\n【性别】女\n【战斗经验】两年\n【出身地】拉特兰\n
【生日】12月24日\n【种族】萨科塔\n【身高】159cm\n【矿石病感染情况】\n参照医学检测报告，确认为非感染者。\n',
'密录1——来信\n别太担心拉特兰人，他们在哪儿都能过得很好。',
'悖论模拟1——拉特兰风格\n能天使擅长以一对多的混战，铳械在她的手上就像玩具一样听话轻巧。并且幸运的是，在能天使想要爆发秀一波操作时，总有些人能和她配合得特别好。
一个认真起来的拉特兰人的射击速度到底能有多快？测试的结果绝对令人大吃一惊。');

INSERT INTO `operator_attribute_info` VALUES ('0143','能天使',50,20000,3,2,1265,744,"远程",1,123,10,11,60);

INSERT INTO `operator_base_info` VALUES ('能天使','0143','狙击——速射手',6,'高台位','女','输出','优先攻击空中目标','0143','0143');

INSERT INTO `skill_info` VALUES ('冲锋模式','能天使', 5, '倾泻子弹，造成中量伤害',  '110%倍率的三连击');
INSERT INTO `skill_info` VALUES ('扫射模式','能天使', 6, '倾泻子弹，造成大量伤害',  '110%倍率的四连击');
INSERT INTO `skill_info` VALUES ('过载模式','能天使', 7, '倾泻子弹，造成巨量伤害',  '110%倍率的五连击');





INSERT INTO `user_info` VALUES ('冬马和纱','123','123456789@qq.com','13511111111','3','能天使','能天使');

drop database arknights;