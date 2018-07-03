CREATE DATABASE home_sys;

CREATE TABLE home_sys.dnf_area (
  id int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  c_name varchar(255) DEFAULT NULL COMMENT '大区名称',
  i_level int(11) DEFAULT NULL COMMENT '是否为父类',
  c_parent varchar(255) DEFAULT NULL COMMENT '父类id',
  PRIMARY KEY (id)
)
ENGINE = INNODB
AUTO_INCREMENT = 1
CHARACTER SET utf8
COLLATE utf8_general_ci
COMMENT = '大区目录';