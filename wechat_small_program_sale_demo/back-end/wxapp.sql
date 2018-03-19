-- phpMyAdmin SQL Dump
-- version 4.4.7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2018-03-19 16:00:54
-- 服务器版本： 5.5.42-log
-- PHP Version: 5.4.41

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `wxapp`
--

-- --------------------------------------------------------

--
-- 表的结构 `comment`
--

CREATE TABLE IF NOT EXISTS `comment` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `com` text NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `comment`
--

INSERT INTO `comment` (`id`, `uid`, `username`, `com`, `time`) VALUES
(2, 1, '甘jc', '这是第一条评论', '2017-04-13 06:11:04'),
(7, 1, '甘jc', '这是第二条评论', '2017-04-13 06:11:04'),
(2, 1, '甘jc', '这是第二条评论', '2017-04-13 06:12:47'),
(7, 1, '甘jc', '这是第二条频率', '2017-04-13 06:12:47'),
(7, 1, '甘jc', '评价', '2017-04-13 08:32:12');

-- --------------------------------------------------------

--
-- 表的结构 `lbMain`
--

CREATE TABLE IF NOT EXISTS `lbMain` (
  `id` int(11) NOT NULL,
  `imgurl` text NOT NULL,
  `pageid` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `lbMain`
--

INSERT INTO `lbMain` (`id`, `imgurl`, `pageid`) VALUES
(1, 'http://onxtlauhq.bkt.clouddn.com/3.jpg', 3),
(2, 'http://onxtlauhq.bkt.clouddn.com/1.jpg', 1),
(3, 'http://onxtlauhq.bkt.clouddn.com/4.jpg', 4),
(4, 'http://onxtlauhq.bkt.clouddn.com/6.jpg', 6);

-- --------------------------------------------------------

--
-- 表的结构 `orderDetail`
--

CREATE TABLE IF NOT EXISTS `orderDetail` (
  `id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `sid` varchar(200) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `place` varchar(200) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `contain` text NOT NULL,
  `price` varchar(50) NOT NULL,
  `state` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `orderDetail`
--

INSERT INTO `orderDetail` (`id`, `uid`, `sid`, `time`, `place`, `phone`, `contain`, `price`, `state`) VALUES
(1, 2, '7,2,', '2017-04-12 11:40:49', '杭州电子科技大学生活区', '15968182251', '汉堡包7小x6,汉堡包2小x7,汉堡包7中x3,汉堡包2中x1,', '35.5', 3),
(2, 2, '7,', '2017-04-13 06:30:05', '杭州电子科技大学生活区', '15968182251', '汉堡包7大x0,', '0', 3),
(3, 2, '7,', '2017-04-13 08:31:13', '杭州电子科技大学生活区', '15968182251', '汉堡包7中x1,', '1', 1),
(4, 2, '7,', '2017-11-29 01:06:47', '杭州电子科技大学生活区', '15968182251', '汉堡包7小x1,汉堡包7小x1,', '1', 0),
(5, 2, '1,7,', '2017-11-29 01:08:36', '杭州电子科技大学生活区', '15968182251', '汉堡包1大x1,汉堡包7小x1,汉堡包7小x1,汉堡包1大x1,', '31', 0);

-- --------------------------------------------------------

--
-- 表的结构 `sellInfo`
--

CREATE TABLE IF NOT EXISTS `sellInfo` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `imgurl` text NOT NULL,
  `price` varchar(20) NOT NULL,
  `tj` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `des` text NOT NULL,
  `specimg` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `sellInfo`
--

INSERT INTO `sellInfo` (`id`, `name`, `imgurl`, `price`, `tj`, `type`, `des`, `specimg`) VALUES
(1, '汉堡包1', 'http://onxtlauhq.bkt.clouddn.com/6.jpg', '5.4/10/15', '', '小,中,大', '阿斯顿垃圾山东矿机', 'http://onxtlauhq.bkt.clouddn.com/6.jpg,http://onxtlauhq.bkt.clouddn.com/5.jpg'),
(2, '汉堡包2', 'http://onxtlauhq.bkt.clouddn.com/0.jpg', '3.5/5/10', '2,http://onxtlauhq.bkt.clouddn.com/ham.png', '小,中,大', '啊实打实大厦大神大神的', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg'),
(3, '汉堡包3', 'http://onxtlauhq.bkt.clouddn.com/1.jpg', '10.1/20', '', '小,大', '阿萨四大四大四大', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg'),
(4, '汉堡包4', 'http://onxtlauhq.bkt.clouddn.com/3.jpg', '1.1/5/9', '3,http://onxtlauhq.bkt.clouddn.com/ham.png', '小,中,大', '啊飒飒大师的发给大范甘迪', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg'),
(5, '汉堡包5', 'http://onxtlauhq.bkt.clouddn.com/2.jpg', '40.1', '', '小', '阿萨斯的权威分公告很反感', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg'),
(6, '汉堡包6', 'http://onxtlauhq.bkt.clouddn.com/4.jpg', '69/70/80', '', '小,中,大', '体育尔特让他玩我', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg'),
(7, '汉堡包7', 'http://onxtlauhq.bkt.clouddn.com/5.jpg', '0.5/1/2', '1,http://onxtlauhq.bkt.clouddn.com/ham.png', '小,中,大', '性别女包女包V型表现层V型', 'http://onxtlauhq.bkt.clouddn.com/1.jpg,http://onxtlauhq.bkt.clouddn.com/2.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `userInfo`
--

CREATE TABLE IF NOT EXISTS `userInfo` (
  `id` int(11) NOT NULL,
  `openid` text NOT NULL,
  `gender` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `logourl` text NOT NULL,
  `buyCar` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `userInfo`
--

INSERT INTO `userInfo` (`id`, `openid`, `gender`, `username`, `address`, `phone`, `logourl`, `buyCar`) VALUES
(2, 'oJB8Z0RqJMVZ3H36mXELjFGqvX_g', 1, '甘jc', '', '', 'https://wx.qlogo.cn/mmopen/vi_32/9xkaQhBrbjIaKgpXWcMkS3v5xuaQD6wVO0ic4MsS0rv3j1bvyk2KkOicBF93dnLHGJeiciahsPp9S2V0pEuLuiby4Tg/0', '7,小,0.5,5');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lbMain`
--
ALTER TABLE `lbMain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orderDetail`
--
ALTER TABLE `orderDetail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sellInfo`
--
ALTER TABLE `sellInfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userInfo`
--
ALTER TABLE `userInfo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lbMain`
--
ALTER TABLE `lbMain`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `orderDetail`
--
ALTER TABLE `orderDetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `sellInfo`
--
ALTER TABLE `sellInfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `userInfo`
--
ALTER TABLE `userInfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
