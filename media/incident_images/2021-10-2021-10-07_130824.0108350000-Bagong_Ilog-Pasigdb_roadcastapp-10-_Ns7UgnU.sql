-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2021 at 05:05 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_roadcastapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_add_departments', 7, 'add_tbl_add_departments'),
(26, 'Can change tbl_add_departments', 7, 'change_tbl_add_departments'),
(27, 'Can delete tbl_add_departments', 7, 'delete_tbl_add_departments'),
(28, 'Can view tbl_add_departments', 7, 'view_tbl_add_departments'),
(29, 'Can add tbl_add_members', 8, 'add_tbl_add_members'),
(30, 'Can change tbl_add_members', 8, 'change_tbl_add_members'),
(31, 'Can delete tbl_add_members', 8, 'delete_tbl_add_members'),
(32, 'Can view tbl_add_members', 8, 'view_tbl_add_members'),
(33, 'Can add tbl_barangay', 9, 'add_tbl_barangay'),
(34, 'Can change tbl_barangay', 9, 'change_tbl_barangay'),
(35, 'Can delete tbl_barangay', 9, 'delete_tbl_barangay'),
(36, 'Can view tbl_barangay', 9, 'view_tbl_barangay'),
(37, 'Can add tbl_district', 10, 'add_tbl_district'),
(38, 'Can change tbl_district', 10, 'change_tbl_district'),
(39, 'Can delete tbl_district', 10, 'delete_tbl_district'),
(40, 'Can view tbl_district', 10, 'view_tbl_district'),
(41, 'Can add tbl_genpub_users', 11, 'add_tbl_genpub_users'),
(42, 'Can change tbl_genpub_users', 11, 'change_tbl_genpub_users'),
(43, 'Can delete tbl_genpub_users', 11, 'delete_tbl_genpub_users'),
(44, 'Can view tbl_genpub_users', 11, 'view_tbl_genpub_users'),
(45, 'Can add tbl_member_type', 12, 'add_tbl_member_type'),
(46, 'Can change tbl_member_type', 12, 'change_tbl_member_type'),
(47, 'Can delete tbl_member_type', 12, 'delete_tbl_member_type'),
(48, 'Can view tbl_member_type', 12, 'view_tbl_member_type'),
(49, 'Can add tbl_position', 13, 'add_tbl_position'),
(50, 'Can change tbl_position', 13, 'change_tbl_position'),
(51, 'Can delete tbl_position', 13, 'delete_tbl_position'),
(52, 'Can view tbl_position', 13, 'view_tbl_position'),
(53, 'Can add tbl_substation', 14, 'add_tbl_substation'),
(54, 'Can change tbl_substation', 14, 'change_tbl_substation'),
(55, 'Can delete tbl_substation', 14, 'delete_tbl_substation'),
(56, 'Can view tbl_substation', 14, 'view_tbl_substation'),
(57, 'Can add tbl_public_report', 15, 'add_tbl_public_report'),
(58, 'Can change tbl_public_report', 15, 'change_tbl_public_report'),
(59, 'Can delete tbl_public_report', 15, 'delete_tbl_public_report'),
(60, 'Can view tbl_public_report', 15, 'view_tbl_public_report'),
(61, 'Can add tbl_pasig_incidents', 16, 'add_tbl_pasig_incidents'),
(62, 'Can change tbl_pasig_incidents', 16, 'change_tbl_pasig_incidents'),
(63, 'Can delete tbl_pasig_incidents', 16, 'delete_tbl_pasig_incidents'),
(64, 'Can view tbl_pasig_incidents', 16, 'view_tbl_pasig_incidents'),
(65, 'Can add tbl_audit', 17, 'add_tbl_audit'),
(66, 'Can change tbl_audit', 17, 'change_tbl_audit'),
(67, 'Can delete tbl_audit', 17, 'delete_tbl_audit'),
(68, 'Can view tbl_audit', 17, 'view_tbl_audit'),
(69, 'Can add tbl_forecast', 18, 'add_tbl_forecast'),
(70, 'Can change tbl_forecast', 18, 'change_tbl_forecast'),
(71, 'Can delete tbl_forecast', 18, 'delete_tbl_forecast'),
(72, 'Can view tbl_forecast', 18, 'view_tbl_forecast'),
(73, 'Can add tbl_public_report_response', 19, 'add_tbl_public_report_response'),
(74, 'Can change tbl_public_report_response', 19, 'change_tbl_public_report_response'),
(75, 'Can delete tbl_public_report_response', 19, 'delete_tbl_public_report_response'),
(76, 'Can view tbl_public_report_response', 19, 'view_tbl_public_report_response');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$SXwrUmkQADn4wMVk1rjCsn$lGPk3P2eN1uJvY2GFjClp1NisyM9NscXpSlG0qPgzLI=', '2021-10-03 07:55:16.361016', 1, 'admin', '', '', 'karenabuan8@gmail.com', 1, 1, '2021-09-24 16:57:07.080053');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-09-24 17:08:40.182527', '1', 'Abuan', 1, '[{\"added\": {}}]', 11, 1),
(2, '2021-09-25 08:29:27.657579', '72', 'Pasig-<django.db.models.query_utils.DeferredAttribute object at 0x00000292A9792B20>-2021-09-25', 1, '[{\"added\": {}}]', 16, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'roadcast', 'tbl_add_departments'),
(8, 'roadcast', 'tbl_add_members'),
(17, 'roadcast', 'tbl_audit'),
(9, 'roadcast', 'tbl_barangay'),
(10, 'roadcast', 'tbl_district'),
(18, 'roadcast', 'tbl_forecast'),
(11, 'roadcast', 'tbl_genpub_users'),
(12, 'roadcast', 'tbl_member_type'),
(16, 'roadcast', 'tbl_pasig_incidents'),
(13, 'roadcast', 'tbl_position'),
(15, 'roadcast', 'tbl_public_report'),
(19, 'roadcast', 'tbl_public_report_response'),
(14, 'roadcast', 'tbl_substation'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-09-24 16:34:54.974878'),
(2, 'auth', '0001_initial', '2021-09-24 16:35:02.687210'),
(3, 'admin', '0001_initial', '2021-09-24 16:35:04.799440'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-09-24 16:35:04.834202'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-09-24 16:35:04.866926'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-09-24 16:35:05.537809'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-09-24 16:35:06.546714'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-09-24 16:35:06.682707'),
(9, 'auth', '0004_alter_user_username_opts', '2021-09-24 16:35:06.706707'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-09-24 16:35:07.134236'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-09-24 16:35:07.168831'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-09-24 16:35:07.208856'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-09-24 16:35:07.288832'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-09-24 16:35:07.360902'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-09-24 16:35:07.432831'),
(16, 'auth', '0011_update_proxy_permissions', '2021-09-24 16:35:07.456832'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-09-24 16:35:07.536870'),
(18, 'roadcast', '0001_initial', '2021-09-24 16:35:20.131771'),
(19, 'sessions', '0001_initial', '2021-09-24 16:35:20.635836'),
(20, 'roadcast', '0002_auto_20210925_1624', '2021-09-25 08:24:59.950627'),
(21, 'roadcast', '0003_auto_20210925_1631', '2021-09-25 08:31:49.645961'),
(22, 'roadcast', '0004_auto_20210925_2324', '2021-09-25 15:25:13.532533'),
(23, 'roadcast', '0005_auto_20210926_1412', '2021-09-26 06:12:26.165595'),
(24, 'roadcast', '0006_auto_20210926_1436', '2021-09-26 06:37:33.381663'),
(25, 'roadcast', '0007_auto_20210926_1443', '2021-09-26 06:43:17.499697'),
(26, 'roadcast', '0008_auto_20210926_1545', '2021-09-26 07:46:34.375788'),
(27, 'roadcast', '0009_auto_20210926_1644', '2021-09-26 08:44:41.120038'),
(28, 'roadcast', '0010_auto_20210926_1715', '2021-09-26 09:15:40.958198'),
(29, 'roadcast', '0011_auto_20210926_1717', '2021-09-26 09:17:56.078859'),
(30, 'roadcast', '0012_auto_20210927_1932', '2021-09-27 11:32:34.656500'),
(31, 'roadcast', '0013_auto_20210927_2256', '2021-09-27 14:57:22.433875'),
(32, 'roadcast', '0014_auto_20210928_0017', '2021-09-27 16:17:07.613696'),
(33, 'roadcast', '0015_auto_20210928_1230', '2021-09-28 04:30:29.727599'),
(34, 'roadcast', '0016_auto_20210928_1242', '2021-09-28 04:42:43.277328'),
(35, 'roadcast', '0017_auto_20210928_1247', '2021-09-28 04:47:22.730461'),
(36, 'roadcast', '0012_auto_20210928_0842', '2021-09-30 01:55:17.886179'),
(37, 'roadcast', '0013_auto_20210928_1808', '2021-09-30 01:55:20.106886'),
(38, 'roadcast', '0018_merge_0013_auto_20210928_1808_0017_auto_20210928_1247', '2021-09-30 01:55:20.189397'),
(39, 'roadcast', '0019_auto_20210930_0955', '2021-09-30 01:55:20.297416'),
(40, 'roadcast', '0020_auto_20210930_1037', '2021-09-30 02:37:30.891431'),
(41, 'roadcast', '0021_auto_20211001_2013', '2021-10-03 02:07:49.980236'),
(42, 'roadcast', '0022_auto_20211003_1007', '2021-10-03 02:18:44.184503'),
(43, 'roadcast', '0023_auto_20211003_1535', '2021-10-03 07:35:40.318155'),
(44, 'roadcast', '0024_auto_20211004_1644', '2021-10-04 08:44:47.398748'),
(45, 'roadcast', '0025_auto_20211004_1654', '2021-10-04 08:54:56.263638'),
(46, 'roadcast', '0002_auto_20211006_1018', '2021-10-06 02:19:06.813945'),
(47, 'roadcast', '0003_auto_20211006_1019', '2021-10-06 02:19:41.752209'),
(48, 'roadcast', '0004_auto_20211006_1020', '2021-10-06 02:20:27.330090'),
(49, 'roadcast', '0005_auto_20211006_1030', '2021-10-06 02:30:53.122935'),
(50, 'roadcast', '0006_auto_20211006_1657', '2021-10-06 09:03:35.385688');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('463p6rh2zqeu14pbz0gbjcbpfdt2dv2f', '.eJxVjEsOwjAMBe-SNYrc0MY1S_Y9Q-XYLimgVOpnhbg7VOoCtm9m3sv1vK253xab-1HdxVXu9LslloeVHeidy23yMpV1HpPfFX_QxXeT2vN6uH8HmZf8rROSIqoRSQsxUKqs4SSRAgELcwODkAISWiuDgFYtEMK5jmg1cnDvD_IHN-o:1mTwWX:P6fVESSff-8Kq43k2H7b0neUy6SfqmnU9Aj4SP4UACc', '2021-10-09 01:30:41.633978'),
('bkl1rqhr81ih2wixj15bnrir4n47dbgj', '.eJxVjEsOwjAMBe-SNYrc0MY1S_Y9Q-XYLimgVOpnhbg7VOoCtm9m3sv1vK253xab-1HdxVXu9LslloeVHeidy23yMpV1HpPfFX_QxXeT2vN6uH8HmZf8rROSIqoRSQsxUKqs4SSRAgELcwODkAISWiuDgFYtEMK5jmg1cnDvD_IHN-o:1mUefa:ZJu7as7-0h0YNHqbo6LFZVLGdSVzwzkcqPy1kJdwRew', '2021-10-11 00:38:58.108876'),
('ushskqgz7h4i8e2q76ynf7o0qn9q9x5n', '.eJxVjEsOwjAMBe-SNYrc0MY1S_Y9Q-XYLimgVOpnhbg7VOoCtm9m3sv1vK253xab-1HdxVXu9LslloeVHeidy23yMpV1HpPfFX_QxXeT2vN6uH8HmZf8rROSIqoRSQsxUKqs4SSRAgELcwODkAISWiuDgFYtEMK5jmg1cnDvD_IHN-o:1mY8Ga:LQA0U2jBMT33-EJiv41i-uKgU9GA6od9bUlXfp_CwEY', '2021-10-20 14:51:32.833072');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_add_departments`
--

CREATE TABLE `roadcast_tbl_add_departments` (
  `id` bigint(20) NOT NULL,
  `Dept_Dept` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_add_departments`
--

INSERT INTO `roadcast_tbl_add_departments` (`id`, `Dept_Dept`) VALUES
(33, 'Anti-Kidnapping Group'),
(34, 'Anti-Cybercrime Group'),
(35, 'Aviation Security Group'),
(36, 'Civil Security Group'),
(37, 'Criminal Investigation and Detection Group'),
(38, 'Drug Enforcement Group'),
(39, 'Highway Patrol Group'),
(40, 'Integrity Monitoring and Enforcement Group'),
(41, 'Intelligence Group'),
(42, 'Maritime Group'),
(43, 'Police Security and Protection Group'),
(44, 'Special Action Force'),
(48, 'Traffic Investigation Team'),
(49, 'Hey'),
(50, 'Hello');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_add_members`
--

CREATE TABLE `roadcast_tbl_add_members` (
  `id` int(11) NOT NULL,
  `Members_District` varchar(200) DEFAULT NULL,
  `Members_Fname` varchar(200) DEFAULT NULL,
  `Members_Lname` varchar(200) DEFAULT NULL,
  `Members_Email` varchar(200) DEFAULT NULL,
  `Members_Password` varchar(200) DEFAULT NULL,
  `Date_Added` date DEFAULT NULL,
  `Added_By` varchar(200) DEFAULT NULL,
  `Members_Pic` varchar(100) DEFAULT NULL,
  `Members_Dept_id` bigint(20) DEFAULT NULL,
  `Members_Position_id` bigint(20) DEFAULT NULL,
  `Members_Substation_id` bigint(20) DEFAULT NULL,
  `Members_User_id` bigint(20) DEFAULT NULL,
  `Date_Edit` date DEFAULT NULL,
  `Edit_By` varchar(200) DEFAULT NULL,
  `Members_Username` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_add_members`
--

INSERT INTO `roadcast_tbl_add_members` (`id`, `Members_District`, `Members_Fname`, `Members_Lname`, `Members_Email`, `Members_Password`, `Date_Added`, `Added_By`, `Members_Pic`, `Members_Dept_id`, `Members_Position_id`, `Members_Substation_id`, `Members_User_id`, `Date_Edit`, `Edit_By`, `Members_Username`) VALUES
(4, 'Pasig', 'Alec', 'Napigkit', 'alec@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.jpg', 34, 8, 3, 1, NULL, 'Have not been editted yet', NULL),
(5, 'Pasig', 'Dane', 'Napigkit', 'dane@pnp.com', 'pnppolice', '2021-09-24', NULL, '2021-09-Dane-HdiSoi0JVC.jpg', 39, 6, 6, 4, NULL, 'Have not been editted yet', NULL),
(6, 'Pasig', 'Ayen', 'Napigkit', 'ayen@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.png', 38, 11, 3, 2, NULL, 'Have not been editted yet', NULL),
(8, 'Pasig', 'Aj', 'Halikana', 'aj@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.png', 39, 11, 6, 4, NULL, 'Have not been editted yet', NULL),
(9, 'Pasig', 'Kim', 'Lara', 'kim@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.png', 40, 7, 8, 4, NULL, 'Have not been editted yet', NULL),
(10, 'Pasig', 'Jew', 'Soliano', 'jew@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.png', 39, 8, 1, 3, NULL, 'Have not been editted yet', NULL),
(11, 'Pasig', 'Koko', 'Chanel', 'koko@pnp.com', 'pnppolice', '2021-09-24', NULL, 'Profile/default.png', 42, 13, 1, 4, NULL, 'Have not been editted yet', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_audit`
--

CREATE TABLE `roadcast_tbl_audit` (
  `id` bigint(20) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `date_logged_in` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_audit`
--

INSERT INTO `roadcast_tbl_audit` (`id`, `username`, `password`, `date_logged_in`) VALUES
(1, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:16:26.212588'),
(2, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:17:15.493177'),
(3, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:25:27.299509'),
(4, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:26:12.086250'),
(5, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:38:54.030020'),
(6, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:39:11.971836'),
(7, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:42:14.111869'),
(8, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:42:43.429653'),
(9, 'admin@gmail.com', 'kfabuan', '2021-09-24 19:44:33.244699'),
(10, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:45:14.350839'),
(11, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:45:54.886283'),
(12, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:46:26.391609'),
(13, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:46:42.381893'),
(14, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:47:17.229971'),
(15, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:49:10.172491'),
(16, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:55:48.684613'),
(17, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:56:12.747186'),
(18, 'kim@pnp.com', 'pnppolice', '2021-09-24 19:58:09.231879'),
(19, 'aj@pnp.com', 'pnppolice', '2021-09-24 20:06:34.070722'),
(20, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:10:30.692738'),
(21, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:11:54.284003'),
(22, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:13:06.654342'),
(23, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:18:17.860292'),
(24, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:26:14.083974'),
(25, 'kim@pnp.com', 'pnppolice', '2021-09-24 20:26:36.853286'),
(26, 'kim@pnp.com', 'pnppolice', '2021-09-24 20:28:06.833089'),
(27, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:28:36.207869'),
(28, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:29:51.368742'),
(29, 'kim@pnp.com', 'pnppolice', '2021-09-24 20:30:04.224188'),
(30, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:30:14.122190'),
(31, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:31:04.223738'),
(32, 'kim@pnp.com', 'pnppolice', '2021-09-24 20:31:16.698070'),
(33, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:31:28.485002'),
(34, 'kim@pnp.com', 'pnppolice', '2021-09-24 20:31:53.874270'),
(35, 'admin@gmail.com', 'kfabuan', '2021-09-24 20:32:22.013580'),
(36, 'aj@pnp.com', 'pnppolice', '2021-09-24 20:32:42.691282'),
(37, 'admin@gmail.com', 'kfabuan', '2021-09-25 01:30:35.595290'),
(38, 'koko@pnp.com', 'pnppolice', '2021-09-26 15:56:22.873097'),
(39, 'karenabuan8@gmail.com', '11111111', '2021-09-27 00:34:42.433328'),
(40, 'karenabuan8@gmail.com', '11111111', '2021-09-27 00:35:56.000316'),
(41, 'alec@pnp.com', 'pnppolice', '2021-10-03 07:56:38.203057'),
(42, 'alec@pnp.com', 'pnppolice', '2021-10-03 08:02:20.124482'),
(43, 'user@gmail.com', 'kfabuan', '2021-10-04 08:22:25.605652'),
(44, 'karenabuan8@gmail.com', '11111111', '2021-10-04 14:58:02.690854'),
(45, 'alec@pnp.com', 'pnppolice', '2021-10-04 15:03:57.267305'),
(46, 'koko@pnp.com', 'pnppolice', '2021-10-05 14:44:53.396261'),
(47, 'ayen@pnp.com', 'pnppolice', '2021-10-05 14:46:45.388741'),
(48, 'user@gmail.com', 'kfabuan', '2021-10-05 14:47:59.256857'),
(49, 'user@gmail.com', 'kfabuan', '2021-10-05 14:48:52.894070'),
(50, 'karenabuan8@gmail.com', '11111111', '2021-10-06 02:36:25.534352'),
(51, 'user@gmail.com', 'kfabuan', '2021-10-06 02:37:42.263940'),
(52, 'alec@pnp.com', 'pnppolice', '2021-10-06 12:47:48.584608'),
(53, 'user@gmail.com', 'kfabuan', '2021-10-06 14:29:45.093662'),
(54, 'alec@pnp.com', 'pnppolice', '2021-10-06 14:30:31.557406'),
(55, 'user@gmail.com', 'kfabuan', '2021-10-06 14:34:06.468169'),
(56, 'alec@pnp.com', 'pnppolice', '2021-10-06 14:37:44.827368'),
(57, 'user@gmail.com', 'kfabuan', '2021-10-06 14:38:37.732400'),
(58, 'alec@pnp.com', 'pnppolice', '2021-10-06 14:39:18.863158'),
(59, 'karenabuan8@gmail.com', '11111111', '2021-10-06 14:40:27.299639'),
(60, 'karenabuan8@gmail.com', '11111111', '2021-10-06 14:46:47.132998'),
(61, 'user@gmail.com', 'kfabuan', '2021-10-06 14:47:12.312998'),
(62, 'alec@pnp.com', 'pnppolice', '2021-10-06 14:50:14.528850'),
(63, 'karenabuan8@gmail.com', '11111111', '2021-10-06 14:51:04.655730');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_barangay`
--

CREATE TABLE `roadcast_tbl_barangay` (
  `id` bigint(20) NOT NULL,
  `Barangay` varchar(200) NOT NULL,
  `District_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_barangay`
--

INSERT INTO `roadcast_tbl_barangay` (`id`, `Barangay`, `District_id_id`) VALUES
(1, 'Ugong', 1),
(2, 'Bagong Ilog', 1),
(3, 'Bambang', 1),
(4, 'Caniogan', 1),
(5, 'Bagong Katipunan', 1),
(6, 'Kalawaan', 1),
(7, 'Kapasigan', 1),
(8, 'Kapitolyo', 1),
(9, 'Malinao', 1),
(10, 'Oranbo', 1),
(11, 'Palatiw', 1),
(12, 'Sagad', 1),
(13, 'San Antonio', 1),
(14, 'San Joaquin', 1),
(15, 'San Jose', 1),
(16, 'San Nicolas', 1),
(17, 'Santo Tomas', 1),
(18, 'Sumilang', 1),
(19, 'Dela Paz', 2),
(20, 'Manggahan', 2),
(21, 'Maybunga', 2),
(22, 'Pinagbuhatan', 2),
(23, 'Rosario', 2),
(24, 'San Miguel', 2),
(25, 'Santa Lucia', 2),
(26, 'Santolan', 2),
(27, 'Buting', 1),
(28, 'Pineda', 1),
(29, 'Santa Cruz', 1),
(30, 'Santa Rosa', 1);

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_district`
--

CREATE TABLE `roadcast_tbl_district` (
  `id` bigint(20) NOT NULL,
  `District` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_district`
--

INSERT INTO `roadcast_tbl_district` (`id`, `District`) VALUES
(1, 'District 1'),
(2, 'District 2');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_forecast`
--

CREATE TABLE `roadcast_tbl_forecast` (
  `Date` date NOT NULL,
  `Incidents` int(10) UNSIGNED NOT NULL CHECK (`Incidents` >= 0),
  `Averages` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_forecast`
--

INSERT INTO `roadcast_tbl_forecast` (`Date`, `Incidents`, `Averages`) VALUES
('2019-01-24', 1, 0),
('2019-01-25', 0, 0),
('2019-01-26', 0, 0),
('2019-01-27', 0, 0),
('2019-01-28', 0, 0),
('2019-01-29', 1, 0),
('2019-01-30', 0, 0.2857),
('2019-01-31', 0, 0.1429),
('2019-02-01', 0, 0.1429),
('2019-02-02', 0, 0.1429),
('2019-02-03', 0, 0.1429),
('2019-02-04', 0, 0.1429),
('2019-02-05', 0, 0),
('2019-02-06', 4, 0.5714),
('2019-02-07', 0, 0.5714),
('2019-02-08', 0, 0.5714),
('2019-02-09', 0, 0.5714),
('2019-02-10', 0, 0.5714),
('2019-02-11', 0, 0.5714),
('2019-02-12', 0, 0.5714),
('2019-02-13', 2, 0.2857),
('2019-02-14', 2, 0.5714),
('2019-02-15', 0, 0.5714),
('2019-02-16', 0, 0.5714),
('2019-02-17', 0, 0.5714),
('2019-02-18', 0, 0.5714),
('2019-02-19', 0, 0.5714),
('2019-02-20', 0, 0.2857),
('2019-02-21', 0, 0),
('2019-02-22', 0, 0),
('2019-02-23', 0, 0),
('2019-02-24', 2, 0.2857),
('2019-02-25', 0, 0.2857),
('2019-02-26', 0, 0.2857),
('2019-02-27', 6, 1.1429),
('2019-02-28', 10, 2.5714),
('2019-03-01', 0, 2.5714),
('2019-03-02', 0, 2.5714),
('2019-03-03', 0, 2.2857),
('2019-03-04', 0, 2.2857),
('2019-03-05', 0, 2.2857),
('2019-03-06', 0, 1.4286),
('2019-03-07', 0, 0),
('2019-03-08', 0, 0),
('2019-03-09', 0, 0),
('2019-03-10', 0, 0),
('2019-03-11', 0, 0),
('2019-03-12', 0, 0),
('2019-03-13', 0, 0),
('2019-03-14', 0, 0),
('2019-03-15', 0, 0),
('2019-03-16', 0, 0),
('2019-03-17', 0, 0),
('2019-03-18', 0, 0),
('2019-03-19', 0, 0),
('2019-03-20', 0, 0),
('2019-03-21', 0, 0),
('2019-03-22', 0, 0),
('2019-03-23', 0, 0),
('2019-03-24', 0, 0),
('2019-03-25', 0, 0),
('2019-03-26', 0, 0),
('2019-03-27', 0, 0),
('2019-03-28', 0, 0),
('2019-03-29', 0, 0),
('2019-03-30', 0, 0),
('2019-03-31', 0, 0),
('2019-04-01', 0, 0),
('2019-04-02', 0, 0),
('2019-04-03', 0, 0),
('2019-04-04', 0, 0),
('2019-04-05', 0, 0),
('2019-04-06', 0, 0),
('2019-04-07', 0, 0),
('2019-04-08', 0, 0),
('2019-04-09', 0, 0),
('2019-04-10', 0, 0),
('2019-04-11', 0, 0),
('2019-04-12', 0, 0),
('2019-04-13', 0, 0),
('2019-04-14', 0, 0),
('2019-04-15', 0, 0),
('2019-04-16', 0, 0),
('2019-04-17', 0, 0),
('2019-04-18', 0, 0),
('2019-04-19', 0, 0),
('2019-04-20', 0, 0),
('2019-04-21', 0, 0),
('2019-04-22', 0, 0),
('2019-04-23', 0, 0),
('2019-04-24', 0, 0),
('2019-04-25', 0, 0),
('2019-04-26', 0, 0),
('2019-04-27', 0, 0),
('2019-04-28', 0, 0),
('2019-04-29', 0, 0),
('2019-04-30', 0, 0),
('2019-05-01', 0, 0),
('2019-05-02', 0, 0),
('2019-05-03', 0, 0),
('2019-05-04', 0, 0),
('2019-05-05', 0, 0),
('2019-05-06', 0, 0),
('2019-05-07', 0, 0),
('2019-05-08', 0, 0),
('2019-05-09', 0, 0),
('2019-05-10', 0, 0),
('2019-05-11', 0, 0),
('2019-05-12', 0, 0),
('2019-05-13', 0, 0),
('2019-05-14', 0, 0),
('2019-05-15', 0, 0),
('2019-05-16', 0, 0),
('2019-05-17', 0, 0),
('2019-05-18', 0, 0),
('2019-05-19', 0, 0),
('2019-05-20', 0, 0),
('2019-05-21', 0, 0),
('2019-05-22', 0, 0),
('2019-05-23', 0, 0),
('2019-05-24', 0, 0),
('2019-05-25', 0, 0),
('2019-05-26', 0, 0),
('2019-05-27', 0, 0),
('2019-05-28', 0, 0),
('2019-05-29', 0, 0),
('2019-05-30', 0, 0),
('2019-05-31', 0, 0),
('2019-06-01', 0, 0),
('2019-06-02', 0, 0),
('2019-06-03', 0, 0),
('2019-06-04', 0, 0),
('2019-06-05', 0, 0),
('2019-06-06', 0, 0),
('2019-06-07', 0, 0),
('2019-06-08', 0, 0),
('2019-06-09', 0, 0),
('2019-06-10', 0, 0),
('2019-06-11', 0, 0),
('2019-06-12', 0, 0),
('2019-06-13', 0, 0),
('2019-06-14', 0, 0),
('2019-06-15', 0, 0),
('2019-06-16', 0, 0),
('2019-06-17', 0, 0),
('2019-06-18', 0, 0),
('2019-06-19', 0, 0),
('2019-06-20', 0, 0),
('2019-06-21', 0, 0),
('2019-06-22', 0, 0),
('2019-06-23', 0, 0),
('2019-06-24', 0, 0),
('2019-06-25', 0, 0),
('2019-06-26', 0, 0),
('2019-06-27', 0, 0),
('2019-06-28', 0, 0),
('2019-06-29', 0, 0),
('2019-06-30', 0, 0),
('2019-07-01', 0, 0),
('2019-07-02', 0, 0),
('2019-07-03', 0, 0),
('2019-07-04', 0, 0),
('2019-07-05', 0, 0),
('2019-07-06', 0, 0),
('2019-07-07', 0, 0),
('2019-07-08', 0, 0),
('2019-07-09', 0, 0),
('2019-07-10', 0, 0),
('2019-07-11', 0, 0),
('2019-07-12', 0, 0),
('2019-07-13', 0, 0),
('2019-07-14', 0, 0),
('2019-07-15', 0, 0),
('2019-07-16', 0, 0),
('2019-07-17', 0, 0),
('2019-07-18', 0, 0),
('2019-07-19', 0, 0),
('2019-07-20', 0, 0),
('2019-07-21', 0, 0),
('2019-07-22', 0, 0),
('2019-07-23', 0, 0),
('2019-07-24', 0, 0),
('2019-07-25', 0, 0),
('2019-07-26', 0, 0),
('2019-07-27', 0, 0),
('2019-07-28', 0, 0),
('2019-07-29', 0, 0),
('2019-07-30', 0, 0),
('2019-07-31', 0, 0),
('2019-08-01', 0, 0),
('2019-08-02', 0, 0),
('2019-08-03', 0, 0),
('2019-08-04', 0, 0),
('2019-08-05', 0, 0),
('2019-08-06', 0, 0),
('2019-08-07', 0, 0),
('2019-08-08', 0, 0),
('2019-08-09', 0, 0),
('2019-08-10', 0, 0),
('2019-08-11', 0, 0),
('2019-08-12', 0, 0),
('2019-08-13', 0, 0),
('2019-08-14', 0, 0),
('2019-08-15', 0, 0),
('2019-08-16', 0, 0),
('2019-08-17', 0, 0),
('2019-08-18', 0, 0),
('2019-08-19', 0, 0),
('2019-08-20', 0, 0),
('2019-08-21', 0, 0),
('2019-08-22', 0, 0),
('2019-08-23', 0, 0),
('2019-08-24', 0, 0),
('2019-08-25', 0, 0),
('2019-08-26', 0, 0),
('2019-08-27', 0, 0),
('2019-08-28', 0, 0),
('2019-08-29', 0, 0),
('2019-08-30', 0, 0),
('2019-08-31', 0, 0),
('2019-09-01', 0, 0),
('2019-09-02', 0, 0),
('2019-09-03', 0, 0),
('2019-09-04', 0, 0),
('2019-09-05', 0, 0),
('2019-09-06', 0, 0),
('2019-09-07', 0, 0),
('2019-09-08', 0, 0),
('2019-09-09', 0, 0),
('2019-09-10', 0, 0),
('2019-09-11', 0, 0),
('2019-09-12', 0, 0),
('2019-09-13', 0, 0),
('2019-09-14', 0, 0),
('2019-09-15', 0, 0),
('2019-09-16', 0, 0),
('2019-09-17', 0, 0),
('2019-09-18', 0, 0),
('2019-09-19', 0, 0),
('2019-09-20', 0, 0),
('2019-09-21', 0, 0),
('2019-09-22', 0, 0),
('2019-09-23', 0, 0),
('2019-09-24', 0, 0),
('2019-09-25', 0, 0),
('2019-09-26', 0, 0),
('2019-09-27', 0, 0),
('2019-09-28', 0, 0),
('2019-09-29', 0, 0),
('2019-09-30', 0, 0),
('2019-10-01', 0, 0),
('2019-10-02', 0, 0),
('2019-10-03', 0, 0),
('2019-10-04', 0, 0),
('2019-10-05', 0, 0),
('2019-10-06', 0, 0),
('2019-10-07', 0, 0),
('2019-10-08', 0, 0),
('2019-10-09', 0, 0),
('2019-10-10', 0, 0),
('2019-10-11', 0, 0),
('2019-10-12', 0, 0),
('2019-10-13', 0, 0),
('2019-10-14', 0, 0),
('2019-10-15', 0, 0),
('2019-10-16', 0, 0),
('2019-10-17', 0, 0),
('2019-10-18', 0, 0),
('2019-10-19', 0, 0),
('2019-10-20', 0, 0),
('2019-10-21', 0, 0),
('2019-10-22', 0, 0),
('2019-10-23', 0, 0),
('2019-10-24', 0, 0),
('2019-10-25', 0, 0),
('2019-10-26', 0, 0),
('2019-10-27', 0, 0),
('2019-10-28', 0, 0),
('2019-10-29', 0, 0),
('2019-10-30', 0, 0),
('2019-10-31', 0, 0),
('2019-11-01', 0, 0),
('2019-11-02', 0, 0),
('2019-11-03', 0, 0),
('2019-11-04', 0, 0),
('2019-11-05', 0, 0),
('2019-11-06', 0, 0),
('2019-11-07', 0, 0),
('2019-11-08', 0, 0),
('2019-11-09', 0, 0),
('2019-11-10', 0, 0),
('2019-11-11', 0, 0),
('2019-11-12', 0, 0),
('2019-11-13', 0, 0),
('2019-11-14', 0, 0),
('2019-11-15', 0, 0),
('2019-11-16', 0, 0),
('2019-11-17', 0, 0),
('2019-11-18', 0, 0),
('2019-11-19', 0, 0),
('2019-11-20', 0, 0),
('2019-11-21', 0, 0),
('2019-11-22', 0, 0),
('2019-11-23', 0, 0),
('2019-11-24', 0, 0),
('2019-11-25', 0, 0),
('2019-11-26', 0, 0),
('2019-11-27', 0, 0),
('2019-11-28', 0, 0),
('2019-11-29', 0, 0),
('2019-11-30', 0, 0),
('2019-12-01', 0, 0),
('2019-12-02', 0, 0),
('2019-12-03', 0, 0),
('2019-12-04', 0, 0),
('2019-12-05', 0, 0),
('2019-12-06', 0, 0),
('2019-12-07', 0, 0),
('2019-12-08', 0, 0),
('2019-12-09', 0, 0),
('2019-12-10', 0, 0),
('2019-12-11', 0, 0),
('2019-12-12', 0, 0),
('2019-12-13', 0, 0),
('2019-12-14', 0, 0),
('2019-12-15', 0, 0),
('2019-12-16', 0, 0),
('2019-12-17', 0, 0),
('2019-12-18', 0, 0),
('2019-12-19', 0, 0),
('2019-12-20', 0, 0),
('2019-12-21', 0, 0),
('2019-12-22', 0, 0),
('2019-12-23', 0, 0),
('2019-12-24', 0, 0),
('2019-12-25', 0, 0),
('2019-12-26', 0, 0),
('2019-12-27', 0, 0),
('2019-12-28', 0, 0),
('2019-12-29', 0, 0),
('2019-12-30', 0, 0),
('2019-12-31', 0, 0),
('2020-01-01', 0, 0),
('2020-01-02', 0, 0),
('2020-01-03', 0, 0),
('2020-01-04', 0, 0),
('2020-01-05', 0, 0),
('2020-01-06', 0, 0),
('2020-01-07', 0, 0),
('2020-01-08', 0, 0),
('2020-01-09', 0, 0),
('2020-01-10', 0, 0),
('2020-01-11', 0, 0),
('2020-01-12', 0, 0),
('2020-01-13', 0, 0),
('2020-01-14', 0, 0),
('2020-01-15', 0, 0),
('2020-01-16', 0, 0),
('2020-01-17', 0, 0),
('2020-01-18', 0, 0),
('2020-01-19', 0, 0),
('2020-01-20', 0, 0),
('2020-01-21', 0, 0),
('2020-01-22', 0, 0),
('2020-01-23', 0, 0),
('2020-01-24', 0, 0),
('2020-01-25', 0, 0),
('2020-01-26', 0, 0),
('2020-01-27', 0, 0),
('2020-01-28', 0, 0),
('2020-01-29', 0, 0),
('2020-01-30', 0, 0),
('2020-01-31', 0, 0),
('2020-02-01', 0, 0),
('2020-02-02', 0, 0),
('2020-02-03', 0, 0),
('2020-02-04', 0, 0),
('2020-02-05', 0, 0),
('2020-02-06', 0, 0),
('2020-02-07', 0, 0),
('2020-02-08', 0, 0),
('2020-02-09', 0, 0),
('2020-02-10', 0, 0),
('2020-02-11', 0, 0),
('2020-02-12', 0, 0),
('2020-02-13', 0, 0),
('2020-02-14', 0, 0),
('2020-02-15', 0, 0),
('2020-02-16', 0, 0),
('2020-02-17', 0, 0),
('2020-02-18', 0, 0),
('2020-02-19', 0, 0),
('2020-02-20', 0, 0),
('2020-02-21', 0, 0),
('2020-02-22', 0, 0),
('2020-02-23', 0, 0),
('2020-02-24', 0, 0),
('2020-02-25', 0, 0),
('2020-02-26', 0, 0),
('2020-02-27', 0, 0),
('2020-02-28', 0, 0),
('2020-02-29', 0, 0),
('2020-03-01', 0, 0),
('2020-03-02', 0, 0),
('2020-03-03', 0, 0),
('2020-03-04', 0, 0),
('2020-03-05', 0, 0),
('2020-03-06', 0, 0),
('2020-03-07', 0, 0),
('2020-03-08', 0, 0),
('2020-03-09', 0, 0),
('2020-03-10', 0, 0),
('2020-03-11', 0, 0),
('2020-03-12', 0, 0),
('2020-03-13', 0, 0),
('2020-03-14', 0, 0),
('2020-03-15', 0, 0),
('2020-03-16', 0, 0),
('2020-03-17', 0, 0),
('2020-03-18', 0, 0),
('2020-03-19', 0, 0),
('2020-03-20', 0, 0),
('2020-03-21', 0, 0),
('2020-03-22', 0, 0),
('2020-03-23', 0, 0),
('2020-03-24', 0, 0),
('2020-03-25', 0, 0),
('2020-03-26', 0, 0),
('2020-03-27', 0, 0),
('2020-03-28', 0, 0),
('2020-03-29', 0, 0),
('2020-03-30', 0, 0),
('2020-03-31', 0, 0),
('2020-04-01', 0, 0),
('2020-04-02', 0, 0),
('2020-04-03', 0, 0),
('2020-04-04', 0, 0),
('2020-04-05', 0, 0),
('2020-04-06', 0, 0),
('2020-04-07', 0, 0),
('2020-04-08', 0, 0),
('2020-04-09', 0, 0),
('2020-04-10', 0, 0),
('2020-04-11', 0, 0),
('2020-04-12', 0, 0),
('2020-04-13', 0, 0),
('2020-04-14', 0, 0),
('2020-04-15', 0, 0),
('2020-04-16', 0, 0),
('2020-04-17', 0, 0),
('2020-04-18', 0, 0),
('2020-04-19', 0, 0),
('2020-04-20', 0, 0),
('2020-04-21', 0, 0),
('2020-04-22', 0, 0),
('2020-04-23', 0, 0),
('2020-04-24', 0, 0),
('2020-04-25', 0, 0),
('2020-04-26', 0, 0),
('2020-04-27', 0, 0),
('2020-04-28', 0, 0),
('2020-04-29', 0, 0),
('2020-04-30', 0, 0),
('2020-05-01', 0, 0),
('2020-05-02', 0, 0),
('2020-05-03', 0, 0),
('2020-05-04', 0, 0),
('2020-05-05', 0, 0),
('2020-05-06', 0, 0),
('2020-05-07', 0, 0),
('2020-05-08', 0, 0),
('2020-05-09', 0, 0),
('2020-05-10', 0, 0),
('2020-05-11', 0, 0),
('2020-05-12', 0, 0),
('2020-05-13', 0, 0),
('2020-05-14', 0, 0),
('2020-05-15', 0, 0),
('2020-05-16', 0, 0),
('2020-05-17', 0, 0),
('2020-05-18', 0, 0),
('2020-05-19', 0, 0),
('2020-05-20', 0, 0),
('2020-05-21', 0, 0),
('2020-05-22', 0, 0),
('2020-05-23', 0, 0),
('2020-05-24', 0, 0),
('2020-05-25', 0, 0),
('2020-05-26', 0, 0),
('2020-05-27', 0, 0),
('2020-05-28', 0, 0),
('2020-05-29', 0, 0),
('2020-05-30', 0, 0),
('2020-05-31', 0, 0),
('2020-06-01', 0, 0),
('2020-06-02', 0, 0),
('2020-06-03', 0, 0),
('2020-06-04', 0, 0),
('2020-06-05', 0, 0),
('2020-06-06', 0, 0),
('2020-06-07', 0, 0),
('2020-06-08', 0, 0),
('2020-06-09', 0, 0),
('2020-06-10', 0, 0),
('2020-06-11', 0, 0),
('2020-06-12', 0, 0),
('2020-06-13', 0, 0),
('2020-06-14', 0, 0),
('2020-06-15', 0, 0),
('2020-06-16', 0, 0),
('2020-06-17', 0, 0),
('2020-06-18', 0, 0),
('2020-06-19', 0, 0),
('2020-06-20', 0, 0),
('2020-06-21', 0, 0),
('2020-06-22', 0, 0),
('2020-06-23', 0, 0),
('2020-06-24', 0, 0),
('2020-06-25', 0, 0),
('2020-06-26', 0, 0),
('2020-06-27', 0, 0),
('2020-06-28', 0, 0),
('2020-06-29', 0, 0),
('2020-06-30', 0, 0),
('2020-07-01', 0, 0),
('2020-07-02', 0, 0),
('2020-07-03', 0, 0),
('2020-07-04', 0, 0),
('2020-07-05', 0, 0),
('2020-07-06', 0, 0),
('2020-07-07', 0, 0),
('2020-07-08', 0, 0),
('2020-07-09', 0, 0),
('2020-07-10', 0, 0),
('2020-07-11', 0, 0),
('2020-07-12', 0, 0),
('2020-07-13', 0, 0),
('2020-07-14', 0, 0),
('2020-07-15', 0, 0),
('2020-07-16', 0, 0),
('2020-07-17', 0, 0),
('2020-07-18', 0, 0),
('2020-07-19', 0, 0),
('2020-07-20', 0, 0),
('2020-07-21', 0, 0),
('2020-07-22', 0, 0),
('2020-07-23', 0, 0),
('2020-07-24', 0, 0),
('2020-07-25', 0, 0),
('2020-07-26', 0, 0),
('2020-07-27', 0, 0),
('2020-07-28', 0, 0),
('2020-07-29', 0, 0),
('2020-07-30', 0, 0),
('2020-07-31', 0, 0),
('2020-08-01', 0, 0),
('2020-08-02', 0, 0),
('2020-08-03', 0, 0),
('2020-08-04', 0, 0),
('2020-08-05', 0, 0),
('2020-08-06', 0, 0),
('2020-08-07', 0, 0),
('2020-08-08', 0, 0),
('2020-08-09', 0, 0),
('2020-08-10', 0, 0),
('2020-08-11', 0, 0),
('2020-08-12', 0, 0),
('2020-08-13', 0, 0),
('2020-08-14', 0, 0),
('2020-08-15', 0, 0),
('2020-08-16', 0, 0),
('2020-08-17', 0, 0),
('2020-08-18', 0, 0),
('2020-08-19', 0, 0),
('2020-08-20', 0, 0),
('2020-08-21', 0, 0),
('2020-08-22', 0, 0),
('2020-08-23', 0, 0),
('2020-08-24', 0, 0),
('2020-08-25', 0, 0),
('2020-08-26', 0, 0),
('2020-08-27', 0, 0),
('2020-08-28', 0, 0),
('2020-08-29', 0, 0),
('2020-08-30', 0, 0),
('2020-08-31', 0, 0),
('2020-09-01', 0, 0),
('2020-09-02', 0, 0),
('2020-09-03', 0, 0),
('2020-09-04', 0, 0),
('2020-09-05', 0, 0),
('2020-09-06', 0, 0),
('2020-09-07', 0, 0),
('2020-09-08', 0, 0),
('2020-09-09', 0, 0),
('2020-09-10', 0, 0),
('2020-09-11', 0, 0),
('2020-09-12', 0, 0),
('2020-09-13', 0, 0),
('2020-09-14', 0, 0),
('2020-09-15', 0, 0),
('2020-09-16', 0, 0),
('2020-09-17', 0, 0),
('2020-09-18', 0, 0),
('2020-09-19', 0, 0),
('2020-09-20', 0, 0),
('2020-09-21', 0, 0),
('2020-09-22', 0, 0),
('2020-09-23', 0, 0),
('2020-09-24', 0, 0),
('2020-09-25', 0, 0),
('2020-09-26', 0, 0),
('2020-09-27', 0, 0),
('2020-09-28', 0, 0),
('2020-09-29', 0, 0),
('2020-09-30', 0, 0),
('2020-10-01', 0, 0),
('2020-10-02', 0, 0),
('2020-10-03', 0, 0),
('2020-10-04', 0, 0),
('2020-10-05', 0, 0),
('2020-10-06', 0, 0),
('2020-10-07', 0, 0),
('2020-10-08', 0, 0),
('2020-10-09', 0, 0),
('2020-10-10', 0, 0),
('2020-10-11', 0, 0),
('2020-10-12', 0, 0),
('2020-10-13', 0, 0),
('2020-10-14', 0, 0),
('2020-10-15', 0, 0),
('2020-10-16', 0, 0),
('2020-10-17', 0, 0),
('2020-10-18', 0, 0),
('2020-10-19', 0, 0),
('2020-10-20', 0, 0),
('2020-10-21', 0, 0),
('2020-10-22', 0, 0),
('2020-10-23', 0, 0),
('2020-10-24', 0, 0),
('2020-10-25', 0, 0),
('2020-10-26', 0, 0),
('2020-10-27', 0, 0),
('2020-10-28', 0, 0),
('2020-10-29', 0, 0),
('2020-10-30', 0, 0),
('2020-10-31', 0, 0),
('2020-11-01', 0, 0),
('2020-11-02', 0, 0),
('2020-11-03', 0, 0),
('2020-11-04', 0, 0),
('2020-11-05', 0, 0),
('2020-11-06', 0, 0),
('2020-11-07', 0, 0),
('2020-11-08', 0, 0),
('2020-11-09', 0, 0),
('2020-11-10', 0, 0),
('2020-11-11', 0, 0),
('2020-11-12', 1, 0.1429),
('2020-11-13', 0, 0.1429),
('2020-11-14', 0, 0.1429),
('2020-11-15', 0, 0.1429),
('2020-11-16', 0, 0.1429),
('2020-11-17', 0, 0.1429),
('2020-11-18', 0, 0.1429),
('2020-11-19', 0, 0),
('2020-11-20', 0, 0),
('2020-11-21', 0, 0),
('2020-11-22', 0, 0),
('2020-11-23', 0, 0),
('2020-11-24', 0, 0),
('2020-11-25', 0, 0),
('2020-11-26', 0, 0),
('2020-11-27', 0, 0),
('2020-11-28', 0, 0),
('2020-11-29', 0, 0),
('2020-11-30', 0, 0),
('2020-12-01', 0, 0),
('2020-12-02', 0, 0),
('2020-12-03', 0, 0),
('2020-12-04', 0, 0),
('2020-12-05', 0, 0),
('2020-12-06', 0, 0),
('2020-12-07', 0, 0),
('2020-12-08', 0, 0),
('2020-12-09', 0, 0),
('2020-12-10', 0, 0),
('2020-12-11', 0, 0),
('2020-12-12', 0, 0),
('2020-12-13', 0, 0),
('2020-12-14', 0, 0),
('2020-12-15', 0, 0),
('2020-12-16', 0, 0),
('2020-12-17', 0, 0),
('2020-12-18', 0, 0),
('2020-12-19', 0, 0),
('2020-12-20', 0, 0),
('2020-12-21', 0, 0),
('2020-12-22', 0, 0),
('2020-12-23', 0, 0),
('2020-12-24', 0, 0),
('2020-12-25', 0, 0),
('2020-12-26', 0, 0),
('2020-12-27', 0, 0),
('2020-12-28', 0, 0),
('2020-12-29', 0, 0),
('2020-12-30', 0, 0),
('2020-12-31', 0, 0),
('2021-01-01', 0, 0),
('2021-01-02', 0, 0),
('2021-01-03', 0, 0),
('2021-01-04', 0, 0),
('2021-01-05', 0, 0),
('2021-01-06', 0, 0),
('2021-01-07', 0, 0),
('2021-01-08', 0, 0),
('2021-01-09', 0, 0),
('2021-01-10', 0, 0),
('2021-01-11', 0, 0),
('2021-01-12', 0, 0),
('2021-01-13', 0, 0),
('2021-01-14', 0, 0),
('2021-01-15', 0, 0),
('2021-01-16', 0, 0),
('2021-01-17', 0, 0),
('2021-01-18', 0, 0),
('2021-01-19', 0, 0),
('2021-01-20', 0, 0),
('2021-01-21', 0, 0),
('2021-01-22', 0, 0),
('2021-01-23', 0, 0),
('2021-01-24', 0, 0),
('2021-01-25', 0, 0),
('2021-01-26', 0, 0),
('2021-01-27', 0, 0),
('2021-01-28', 0, 0),
('2021-01-29', 0, 0),
('2021-01-30', 0, 0),
('2021-01-31', 0, 0),
('2021-02-01', 0, 0),
('2021-02-02', 0, 0),
('2021-02-03', 0, 0),
('2021-02-04', 0, 0),
('2021-02-05', 0, 0),
('2021-02-06', 0, 0),
('2021-02-07', 0, 0),
('2021-02-08', 0, 0),
('2021-02-09', 0, 0),
('2021-02-10', 0, 0),
('2021-02-11', 0, 0),
('2021-02-12', 0, 0),
('2021-02-13', 0, 0),
('2021-02-14', 0, 0),
('2021-02-15', 0, 0),
('2021-02-16', 0, 0),
('2021-02-17', 0, 0),
('2021-02-18', 0, 0),
('2021-02-19', 0, 0),
('2021-02-20', 0, 0),
('2021-02-21', 0, 0),
('2021-02-22', 0, 0),
('2021-02-23', 0, 0),
('2021-02-24', 0, 0),
('2021-02-25', 0, 0),
('2021-02-26', 0, 0),
('2021-02-27', 0, 0),
('2021-02-28', 0, 0),
('2021-03-01', 0, 0),
('2021-03-02', 0, 0),
('2021-03-03', 0, 0),
('2021-03-04', 0, 0),
('2021-03-05', 0, 0),
('2021-03-06', 0, 0),
('2021-03-07', 0, 0),
('2021-03-08', 0, 0),
('2021-03-09', 0, 0),
('2021-03-10', 0, 0),
('2021-03-11', 0, 0),
('2021-03-12', 0, 0),
('2021-03-13', 0, 0),
('2021-03-14', 0, 0),
('2021-03-15', 0, 0),
('2021-03-16', 0, 0),
('2021-03-17', 0, 0),
('2021-03-18', 0, 0),
('2021-03-19', 0, 0),
('2021-03-20', 0, 0),
('2021-03-21', 0, 0),
('2021-03-22', 0, 0),
('2021-03-23', 0, 0),
('2021-03-24', 0, 0),
('2021-03-25', 0, 0),
('2021-03-26', 0, 0),
('2021-03-27', 0, 0),
('2021-03-28', 0, 0),
('2021-03-29', 0, 0),
('2021-03-30', 0, 0),
('2021-03-31', 0, 0),
('2021-04-01', 0, 0),
('2021-04-02', 0, 0),
('2021-04-03', 0, 0),
('2021-04-04', 0, 0),
('2021-04-05', 0, 0),
('2021-04-06', 0, 0),
('2021-04-07', 0, 0),
('2021-04-08', 0, 0),
('2021-04-09', 0, 0),
('2021-04-10', 0, 0),
('2021-04-11', 0, 0),
('2021-04-12', 0, 0),
('2021-04-13', 0, 0),
('2021-04-14', 0, 0),
('2021-04-15', 0, 0),
('2021-04-16', 0, 0),
('2021-04-17', 0, 0),
('2021-04-18', 0, 0),
('2021-04-19', 0, 0),
('2021-04-20', 0, 0),
('2021-04-21', 0, 0),
('2021-04-22', 0, 0),
('2021-04-23', 0, 0),
('2021-04-24', 0, 0),
('2021-04-25', 0, 0),
('2021-04-26', 0, 0),
('2021-04-27', 0, 0),
('2021-04-28', 0, 0),
('2021-04-29', 0, 0),
('2021-04-30', 0, 0),
('2021-05-01', 0, 0),
('2021-05-02', 0, 0),
('2021-05-03', 0, 0),
('2021-05-04', 0, 0),
('2021-05-05', 0, 0),
('2021-05-06', 0, 0),
('2021-05-07', 0, 0),
('2021-05-08', 0, 0),
('2021-05-09', 0, 0),
('2021-05-10', 0, 0),
('2021-05-11', 0, 0),
('2021-05-12', 0, 0),
('2021-05-13', 0, 0),
('2021-05-14', 0, 0),
('2021-05-15', 0, 0),
('2021-05-16', 0, 0),
('2021-05-17', 0, 0),
('2021-05-18', 0, 0),
('2021-05-19', 0, 0),
('2021-05-20', 0, 0),
('2021-05-21', 0, 0),
('2021-05-22', 0, 0),
('2021-05-23', 0, 0),
('2021-05-24', 0, 0),
('2021-05-25', 0, 0),
('2021-05-26', 0, 0),
('2021-05-27', 0, 0),
('2021-05-28', 0, 0),
('2021-05-29', 0, 0),
('2021-05-30', 0, 0),
('2021-05-31', 0, 0),
('2021-06-01', 0, 0),
('2021-06-02', 0, 0),
('2021-06-03', 0, 0),
('2021-06-04', 0, 0),
('2021-06-05', 0, 0),
('2021-06-06', 0, 0),
('2021-06-07', 0, 0),
('2021-06-08', 0, 0),
('2021-06-09', 0, 0),
('2021-06-10', 0, 0),
('2021-06-11', 0, 0),
('2021-06-12', 0, 0),
('2021-06-13', 0, 0),
('2021-06-14', 0, 0),
('2021-06-15', 0, 0),
('2021-06-16', 0, 0),
('2021-06-17', 0, 0),
('2021-06-18', 0, 0),
('2021-06-19', 0, 0),
('2021-06-20', 0, 0),
('2021-06-21', 0, 0),
('2021-06-22', 0, 0),
('2021-06-23', 0, 0),
('2021-06-24', 0, 0),
('2021-06-25', 0, 0),
('2021-06-26', 0, 0),
('2021-06-27', 0, 0),
('2021-06-28', 0, 0),
('2021-06-29', 0, 0),
('2021-06-30', 0, 0),
('2021-07-01', 0, 0),
('2021-07-02', 0, 0),
('2021-07-03', 0, 0),
('2021-07-04', 0, 0),
('2021-07-05', 0, 0),
('2021-07-06', 0, 0),
('2021-07-07', 0, 0),
('2021-07-08', 0, 0),
('2021-07-09', 0, 0),
('2021-07-10', 0, 0),
('2021-07-11', 0, 0),
('2021-07-12', 0, 0),
('2021-07-13', 0, 0),
('2021-07-14', 0, 0),
('2021-07-15', 0, 0),
('2021-07-16', 0, 0),
('2021-07-17', 0, 0),
('2021-07-18', 0, 0),
('2021-07-19', 0, 0),
('2021-07-20', 0, 0),
('2021-07-21', 0, 0),
('2021-07-22', 0, 0),
('2021-07-23', 0, 0),
('2021-07-24', 0, 0),
('2021-07-25', 0, 0),
('2021-07-26', 0, 0),
('2021-07-27', 0, 0),
('2021-07-28', 0, 0),
('2021-07-29', 0, 0),
('2021-07-30', 0, 0),
('2021-07-31', 0, 0),
('2021-08-01', 0, 0),
('2021-08-02', 0, 0),
('2021-08-03', 0, 0),
('2021-08-04', 0, 0),
('2021-08-05', 0, 0),
('2021-08-06', 0, 0),
('2021-08-07', 0, 0),
('2021-08-08', 1, 0.1429),
('2021-08-09', 0, 0.1429),
('2021-08-10', 0, 0.1429),
('2021-08-11', 0, 0.1429),
('2021-08-12', 0, 0.1429),
('2021-08-13', 0, 0.1429),
('2021-08-14', 0, 0.1429),
('2021-08-15', 0, 0),
('2021-08-16', 0, 0),
('2021-08-17', 0, 0),
('2021-08-18', 0, 0),
('2021-08-19', 0, 0),
('2021-08-20', 0, 0),
('2021-08-21', 0, 0),
('2021-08-22', 0, 0),
('2021-08-23', 0, 0),
('2021-08-24', 0, 0),
('2021-08-25', 0, 0),
('2021-08-26', 0, 0),
('2021-08-27', 0, 0),
('2021-08-28', 0, 0),
('2021-08-29', 0, 0),
('2021-08-30', 0, 0),
('2021-08-31', 0, 0),
('2021-09-01', 0, 0),
('2021-09-02', 0, 0),
('2021-09-03', 0, 0),
('2021-09-04', 1, 0.1429),
('2021-09-05', 0, 0.1429),
('2021-09-06', 1, 0.2857),
('2021-09-07', 1, 0.4286),
('2021-09-08', 6, 1.2857),
('2021-09-09', 1, 1.4286),
('2021-09-10', 2, 1.7143),
('2021-09-11', 0, 1.5714),
('2021-09-12', 0, 1.5714),
('2021-09-13', 0, 1.4286),
('2021-09-14', 1, 1.4286),
('2021-09-15', 0, 0.5714),
('2021-09-16', 0, 0.4286),
('2021-09-17', 0, 0.1429),
('2021-09-18', 0, 0.1429),
('2021-09-19', 0, 0.1429),
('2021-09-20', 3, 0.5714),
('2021-09-21', 3, 0.8571),
('2021-09-22', 0, 0.8571),
('2021-09-23', 0, 0.8571),
('2021-09-24', 1, 1),
('2021-09-25', 1, 1.1429),
('2021-09-26', 1, 1.2857),
('2021-09-27', 1, 1),
('2021-09-28', 0, 0.5714),
('2021-09-29', 0, 0.5714),
('2021-09-30', 2, 0.8571),
('2021-10-01', 3, 1.1429),
('2021-10-02', 1, 1.1429),
('2021-10-03', 1, 1.1429),
('2021-10-04', 1, 1.1429),
('2021-10-05', 0, 1.1429),
('2021-10-06', 1, 1.2857),
('2021-10-07', 0, 1),
('2021-10-08', 0, 0.5714),
('2021-10-09', 0, 0.4286),
('2021-10-10', 0, 0.2857),
('2021-10-11', 0, 0.1429),
('2021-10-12', 0, 0.1429);

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_genpub_users`
--

CREATE TABLE `roadcast_tbl_genpub_users` (
  `id` bigint(20) NOT NULL,
  `gen_surname` varchar(50) DEFAULT NULL,
  `gen_fname` varchar(50) DEFAULT NULL,
  `gen_sex` varchar(50) DEFAULT NULL,
  `gen_bday` datetime(6) DEFAULT NULL,
  `gen_region` varchar(50) DEFAULT NULL,
  `gen_province` varchar(50) DEFAULT NULL,
  `gen_city` varchar(50) DEFAULT NULL,
  `gen_barangay` varchar(50) DEFAULT NULL,
  `gen_contact_no` varchar(50) DEFAULT NULL,
  `gen_username` varchar(50) DEFAULT NULL,
  `gen_pass` varchar(50) DEFAULT NULL,
  `gen_valid_id` varchar(50) DEFAULT NULL,
  `gen_upload_id` varchar(100) DEFAULT NULL,
  `date_signed_up` datetime(6) DEFAULT NULL,
  `Read_Status` varchar(200) NOT NULL,
  `date_edit` date DEFAULT NULL,
  `gen_profile` varchar(100) DEFAULT NULL,
  `is_email_verified` tinyint(1) NOT NULL,
  `is_verified` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_genpub_users`
--

INSERT INTO `roadcast_tbl_genpub_users` (`id`, `gen_surname`, `gen_fname`, `gen_sex`, `gen_bday`, `gen_region`, `gen_province`, `gen_city`, `gen_barangay`, `gen_contact_no`, `gen_username`, `gen_pass`, `gen_valid_id`, `gen_upload_id`, `date_signed_up`, `Read_Status`, `date_edit`, `gen_profile`, `is_email_verified`, `is_verified`) VALUES
(1, 'Williams', 'Yelyah', 'Female', '1999-08-29 16:00:00.000000', 'None', 'None', 'Pasig', 'Santa Lucia', '09163709362', 'user@gmail.com', 'kfabuan', 'Tin ID', 'Public/default.jpg', '2021-09-24 17:08:40.162497', '', '2021-10-04', 'Public/2021-10-hayley1-AFPqEhQziO.jpg', 1, 1),
(2, 'Abwan', 'Fayt', 'Female', '2019-05-28 16:00:00.000000', '2', '1', '1', 'Santa Lucia', '09163709362', 'karenabuan8@gmail.com', '11111111', 'PhilHealth ID', 'Public/2021-09-118659-okjhm0AkKi.jpg', '2021-09-27 00:34:33.503463', '', '2021-10-04', 'Public/2021-10-52993909_617220795367438_6105468260927406080_n-Tdp54z1rgT.jpg', 1, 1),
(3, 'Abuan', 'Karen', 'Female', '2021-08-08 16:00:00.000000', '1', '3', '2', 'Santa Lucia', '09163709362', '20181052@fit.edu.ph', '11111111', 'Passport', 'Public/2021-10-1-xJtaCAJVkB.jpg', '2021-10-03 07:42:05.121842', '', NULL, 'Public/default.jpg', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_member_type`
--

CREATE TABLE `roadcast_tbl_member_type` (
  `id` bigint(20) NOT NULL,
  `Member_Type` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_member_type`
--

INSERT INTO `roadcast_tbl_member_type` (`id`, `Member_Type`) VALUES
(1, 'Admin'),
(2, 'Crime Statistician'),
(3, 'Sub-representative'),
(4, 'Investigator');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_pasig_incidents`
--

CREATE TABLE `roadcast_tbl_pasig_incidents` (
  `id` bigint(20) NOT NULL,
  `City` varchar(200) DEFAULT NULL,
  `UnitStation` varchar(200) DEFAULT NULL,
  `CrimeOffense` varchar(200) DEFAULT NULL,
  `Week` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time(6) DEFAULT NULL,
  `Day` varchar(200) DEFAULT NULL,
  `Incident_Type` varchar(200) DEFAULT NULL,
  `Number_of_Persons_Involved` int(11) DEFAULT NULL,
  `Light` varchar(200) DEFAULT NULL,
  `Weather` varchar(200) DEFAULT NULL,
  `Case_Status` varchar(200) DEFAULT NULL,
  `District_id` bigint(20) DEFAULT NULL,
  `Barangay_id_id` bigint(20) DEFAULT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Along` varchar(200) DEFAULT NULL,
  `Corner` varchar(200) DEFAULT NULL,
  `Latitude` varchar(200) DEFAULT NULL,
  `Longitude` varchar(200) DEFAULT NULL,
  `Surface_Condition` varchar(200) DEFAULT NULL,
  `Surface_Type` varchar(200) DEFAULT NULL,
  `Road_Repair` varchar(200) DEFAULT NULL,
  `Hit_and_Run` varchar(200) DEFAULT NULL,
  `Road_Character` varchar(200) DEFAULT NULL,
  `Suspect_Type` varchar(200) DEFAULT NULL,
  `Suspect_Fname` varchar(200) DEFAULT NULL,
  `Suspect_Lname` varchar(200) DEFAULT NULL,
  `Suspect_Severity` varchar(200) DEFAULT NULL,
  `Suspect_Age` int(11) DEFAULT NULL,
  `Suspect_Sex` varchar(200) DEFAULT NULL,
  `Suspect_Civil_Status` varchar(200) DEFAULT NULL,
  `Suspect_Address` varchar(200) DEFAULT NULL,
  `Suspect_Vehicle` varchar(200) DEFAULT NULL,
  `Suspect_Vehicle_Body_Type` varchar(200) DEFAULT NULL,
  `Suspect_Plate_No` varchar(200) DEFAULT NULL,
  `Suspect_Reg_Owner` varchar(200) DEFAULT NULL,
  `Suspect_Drl_No` varchar(200) DEFAULT NULL,
  `Suspect_Drl_Exp` date DEFAULT NULL,
  `Victim_Type` varchar(200) DEFAULT NULL,
  `Victim_Fname` varchar(200) DEFAULT NULL,
  `Victim_Lname` varchar(200) DEFAULT NULL,
  `Victim_Severity` varchar(200) DEFAULT NULL,
  `Victim_Age` int(11) DEFAULT NULL,
  `Victim_Sex` varchar(200) DEFAULT NULL,
  `Victim_Civil_Status` varchar(200) DEFAULT NULL,
  `Victim_Address` varchar(200) DEFAULT NULL,
  `Victim_Vehicle` varchar(200) DEFAULT NULL,
  `Victim_Vehicle_Body_Type` varchar(200) DEFAULT NULL,
  `Victim_Plate_No` varchar(200) DEFAULT NULL,
  `Victim_Reg_Owner` varchar(200) DEFAULT NULL,
  `Victim_Drl_No` varchar(200) DEFAULT NULL,
  `Victim_Drl_Exp` date DEFAULT NULL,
  `Narrative` varchar(900) DEFAULT NULL,
  `Investigator_id` int(11) DEFAULT NULL,
  `date_added` date DEFAULT NULL,
  `added_by` varchar(200) DEFAULT NULL,
  `archive` varchar(200) DEFAULT NULL,
  `read_status` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_pasig_incidents`
--

INSERT INTO `roadcast_tbl_pasig_incidents` (`id`, `City`, `UnitStation`, `CrimeOffense`, `Week`, `Date`, `Time`, `Day`, `Incident_Type`, `Number_of_Persons_Involved`, `Light`, `Weather`, `Case_Status`, `District_id`, `Barangay_id_id`, `Address`, `Along`, `Corner`, `Latitude`, `Longitude`, `Surface_Condition`, `Surface_Type`, `Road_Repair`, `Hit_and_Run`, `Road_Character`, `Suspect_Type`, `Suspect_Fname`, `Suspect_Lname`, `Suspect_Severity`, `Suspect_Age`, `Suspect_Sex`, `Suspect_Civil_Status`, `Suspect_Address`, `Suspect_Vehicle`, `Suspect_Vehicle_Body_Type`, `Suspect_Plate_No`, `Suspect_Reg_Owner`, `Suspect_Drl_No`, `Suspect_Drl_Exp`, `Victim_Type`, `Victim_Fname`, `Victim_Lname`, `Victim_Severity`, `Victim_Age`, `Victim_Sex`, `Victim_Civil_Status`, `Victim_Address`, `Victim_Vehicle`, `Victim_Vehicle_Body_Type`, `Victim_Plate_No`, `Victim_Reg_Owner`, `Victim_Drl_No`, `Victim_Drl_Exp`, `Narrative`, `Investigator_id`, `date_added`, `added_by`, `archive`, `read_status`) VALUES
(1, 'Pasig', 'Pasig City Police Station', '', 4, '2021-09-06', '18:45:00.000000', '', 'Damage to Property', 2, 'Daylight', 'Sun', 'Solved', 1, 5, 'None', '', '', NULL, NULL, 'Dry', 'Soil', '', '', 'Straight Flat', '', 'None', 'None', '', 44, '', '', 'None', 'None', '', 'None', 'None', 'None', '2021-09-15', '', 'None', 'None', '', 34, '', '', 'None', 'None', '', 'None', 'None', 'None', '2021-09-07', 'hfhfhdfhfhdfhfheh', 8, NULL, '', NULL, 'Yes'),
(2, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 5, '2019-01-29', '23:00:00.000000', 'Tuesday', 'Rear End Collision', 2, 'Night', 'Fair', 'Solved', 2, 20, 'ALONG HON. BENITO SOLIVEN AVE BRGY MANGGAHAN PASIG CITY', 'Hon Benito Soliven', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 39, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 0, 'Male', '', '', '', 'Sedan', '', '', '', NULL, 'T.  D.  P.  O.:\n\nTIME          : 11:00 pm\nDATE          : January 29, 2019 \nDAY           : Tuesday\nPLACE         : Along Hon. Benito Soliven Avenue, Brgy. Manggahan, Pasig City\n\nCOLLISION TYPE: Rear ', NULL, NULL, '', NULL, 'Yes'),
(3, 'Pasig', 'Pasig City Police Station', '', 6, '2019-02-06', '10:20:00.000000', '', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 2, 25, 'ortigas', 'Ortigas Extension', '', '10.345', '12.45', 'Dry', '', '', '', '', '', 'None', 'None', '', 29, 'Male', '', '', '', 'Jitney', '', '', '', '2021-10-07', '', 'None', 'None', '', 18, 'Male', '', 'ALONG ORTIGAS AVE EXT BRGY STA LUCIA PASIG CITY', '', '', '', '', '', '2021-10-07', '                            \r\nT.  D.  P.  O.:\r\nTIME:  01:30 am\r\nDATE:  March 05, 2019\r\nDAY:   Tuesday\r\nPLACE: Along Ortigas avenue extension Brgy. Sta Lucia, Pasig City.\r\n\r\nCOLLISION TYPE: Side/swipe\r\nWEATHER       : Fair               \r\n                        ', 5, NULL, '', NULL, 'Yes'),
(4, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 6, '2019-02-06', '19:30:00.000000', 'Wednesday', 'Others', 2, 'Night', '', 'Solved', 2, 24, 'ALONG C RAYMUNDO AVE COR MERCEDES AVE BRGY SAN MIGUEL PASIG CITY', 'C. Raymundo', 'Mercedes', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 40, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 37, 'Male', '', '', '', 'Tricycle', '', '', '', NULL, '\nT.  D.  P.  O.:\n\nTIME:        11:45 a.m.\nDATE:        5 March 2019\nDAY:         Tuesday\nPLACE:    Along C. Raymundo Avenue (Northeast Direction) corner Mercedes Avenue, Brgy. San Miguel, Pasig City.\n', NULL, NULL, '', NULL, 'Yes'),
(5, 'Pasig', 'Pasig City Police Station', 'Damage to Property, Physical Injury', 7, '2019-02-13', '23:15:00.000000', 'Wednesday', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 1, 1, 'ORTIGAS AVE COR PONTERA DRIVE BRGY UGONG PC', 'Ortigas Extension', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 52, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 29, 'Male', '', '', '', 'Truck', '', '', '', NULL, 'T.  D.  P.  O.:\nTIME:  01:00 am\nDATE:  March 12, 2019\nDAY:   Tuesday\nPLACE: Along C5 road in-front of Arcovia (north bound) Brgy. Ugong, Pasig City.\n\nCOLLISION TYPE: Side/swipe\nWEATHER       : Fair   ', NULL, '0000-00-00', '', NULL, 'No'),
(6, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 7, '2019-02-14', '20:40:00.000000', 'Thursday', 'Sideswiped', 2, 'Night', '', 'Solved', 2, 21, 'ALONG C RAYMUNDO AVE BRGY MAYBUNGA PASIG CITY', 'C. Raymundo', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 50, 'Female', '', '', '', 'SUV', '', '', '', NULL, '', NULL, NULL, '', 0, '', '', '', '', 'Sedan', '', '', '', NULL, '\nT.  D.  P.  O.:\n\nTIME:     08:40 p.m.\nDATE:     14 February 2019\nDAY:      Thursday\nPLACE:   Along C. Raymundo Avenue (Southwest Direction- infront of Logistikus), Brgy. Maybunga, Pasig City.\n\nVEHICL', NULL, '0000-00-00', '', NULL, 'No'),
(7, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-24', '02:30:00.000000', 'Sunday', 'Rear End Collision', 2, 'Night', 'Fair', 'Solved', 2, 23, 'ALONG ORTIGAS AVENUE EXT BRGY ROSARIO PASIG CITY', 'Ortigas Extension', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 41, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 0, '', '', '', '', 'Suv', '', '', '', NULL, '\nT.  D.  P.  O.:\n\nTIME          : 2:30 am\nDATE          : February 24, 2019 \nDAY           : Sunday \nPLACE         : Along Ortigas Avenue Extension, Brgy. Rosario, Pasig City\n\nCOLLISION TYPE: Rear End', NULL, '0000-00-00', '', NULL, 'No'),
(8, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-27', '12:00:00.000000', 'Wednesday', 'Sideswiped', 2, 'Daylight', 'Fair', 'Solved', 1, 11, 'ALONG M.H DEL PILAR ST. BRGY PALATIW PASIG CITY', '', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 24, 'Male', '', '', '', 'Sedan', '', '', '', NULL, '', NULL, NULL, '', 28, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, 'TYPE OF INCIDENT\nRIRI-DTP Date & Time Reported\nMarch 2, 2019/07:30 pm\n\nT.  D.  P.  O.:\n\nTIME          : 12:00 noon\nDATE          : February 27, 2019 \nDAY           : Wednesday\nPLACE         : Along M.', NULL, '0000-00-00', '', NULL, 'No'),
(9, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-27', '13:30:00.000000', 'Wednesday', 'Rear End Collision', 2, 'Daylight', '', 'Solved', 1, 1, 'ALONG ORTIGAS AVENUE WESTBOUND UGONG, PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 22, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, '', NULL, NULL, '', 0, '', '', '', '', 'Unidentified', '', '', '', NULL, 'Type Of Incident:\nRIRI- PI with DTP (HAR)\nCollision Type:\nRear End\n\nT.  D.  P.  O.:\n\nTIME:       01:30 p.m.\nDATE:       27 February 2019\nDAY:        Wednesday\nPLACE:     Along Ortigas Avenue Fly over ', NULL, '0000-00-00', '', NULL, 'No'),
(10, 'Pasig', 'Pasig City Police Station', 'Self Accident', 9, '2019-02-28', '03:30:00.000000', 'Thursday', 'Self Accident', 2, 'Night', 'Fair', 'Solved', 1, 6, 'ALONG ELISCO ROAD KALAWAAN PASIG CITY', '', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 38, 'Male', '', '', '', 'Motorcycle ', '', '', '', NULL, '', NULL, NULL, '', 0, '', '', '', '', '', '', '', '', NULL, 'TYPE OF INCIDENT:\nReckless Imprudence Resulting in Damage to Property & Physical Injury  (RIRI/DTP/PI)  DATE/TIME OF INCIDENT:\nFebruary 21, 2019/ 2430H\nDATE/TIME OF REPORTED:\nFebruary 21,2019/ 0330H  ', NULL, '0000-00-00', '', NULL, 'No'),
(11, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-28', '12:00:00.000000', 'Thursday', 'Angle Collision', 2, 'Daylight', 'Fair', 'Solved', 2, 25, 'ALONG ORTIGAS AVE. EXT. BRGY STA LUCIA PASIG CITY', 'Ortigas Extension', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 38, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, '', NULL, NULL, '', 26, 'Male', '', '', '', 'Ice Cream Cart', '', '', '', NULL, 'TYPE OF INCIDENT\nRIRI-DTP/PI\n\nT.  D.  P.  O.:\n\nTIME          : 12:00 nn\nDATE          : February 28, 2019 \nDAY           : Thursday \nPLACE         : Along Ortigas Avenue Extension, Brgy. Sta. Lucia, P', NULL, '0000-00-00', '', NULL, 'No'),
(12, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-28', '14:30:00.000000', 'Thursday', 'Sideswiped', 2, 'Daylight', 'Fair', 'Solved', 2, 23, 'ALONG ORTIGAS AVE. EXT. BRGY ROSARIO PASIG CITY ', 'Ortigas Extension', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 68, 'Male', '', '', '', 'Sedan', '', '', '', NULL, '', NULL, NULL, '', 43, 'Male', '', '', '', 'Truck', '', '', '', NULL, 'TYPE OF INCIDENT\nRIRI-DTP\n\nT.  D.  P.  O.:\n\nTIME          : 1430H \nDATE          : February 28, 2019 \nDAY           : Thursday \nPLACE         : Along Ortigas Avenue Extension, Brgy. Rosario, Pasig Cit', NULL, '0000-00-00', '', NULL, 'No'),
(13, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-28', '17:00:00.000000', 'Thursday', 'Sideswiped', 2, 'Daylight', '', 'Solved', 2, 24, 'ALONG MARKET AVE. COR. DR. PILAPIL STREET BRGY.SAN MIGUEL, PASIG CITY.', 'Market', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 46, 'Male', '', '', '', 'PUJ', '', '', '', NULL, '', NULL, NULL, '', 43, 'Male', '', '', '', 'Van', '', '', '', NULL, 'Type Of Incident:\nRIRI- DTP\nCollision Type:\nSideswiped\n\nT.  D.  P.  O.:\n\nTIME:        05:00 p.m.\nDATE:        28 February 2019\nDAY:         Thursday\nPLACE:     Along Market Avenue (North Bound) corner', NULL, '0000-00-00', '', NULL, 'No'),
(14, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-28', '18:30:00.000000', 'Thursday', 'Rear End Collision', 2, 'Night', '', 'Solved', 2, 25, 'ALONG ORTIGAS AVE. EXT. COR. SM EAST ORTIGAS COMPOUND BRGY. STA LUCIA, PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 24, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, '', NULL, NULL, '', 49, 'Male', '', '', '', 'PUJ', '', '', '', NULL, 'Type Of Incident:\nRIRI- PI with DTP\nCollision Type:\nRear End\n\nT.  D.  P.  O.:\n\nTIME:       06:30 p.m.\nDATE:       28 February 2019\nDAY:        Thursday\nPLACE:     Along Ortigas Avenue Extension (East ', NULL, '0000-00-00', '', NULL, 'No'),
(15, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-28', '19:40:00.000000', 'Thursday', 'Side Impact', 2, 'Night', 'Fair', 'Solved', 2, 21, 'ALONG LEGASPI ST. INFRONT OF PARKWOOD SUBD. BRGY MAYBUNGA PASIG CITY', '', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 46, 'Male', '', '', '', 'SUV', '', '', '', NULL, '', NULL, NULL, '', 22, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, 'Type Of Incident:\nRIRI- DTP Date & Time Reported\n28 February 2019\n08:45 p.m.\nCollision Type:\nSide Impact  Weather Condition:\nClear/ Fair\n\nT.  D.  P.  O.:\n\nTIME:       07:40 p.m.\nDATE:       28 Februar', NULL, '0000-00-00', '', NULL, 'No'),
(16, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-28', '20:10:00.000000', 'Thursday', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 2, 23, 'ALONG ORTIGAS AVENUE EXT. COR. ST. JOSEPH, BRGY. ROSARIO PASIG CITY', 'Ortigas Extension', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 67, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 41, 'Male', '', '', '', 'Wagon', '', '', '', NULL, 'TYPE OF INCIDENT\nRIRI-DTP\n\nT.  D.  P.  O.:\n\nTIME          : 2010H\nDATE          : February 28, 2019 \nDAY           : Thursday\nPLACE         : Along Ortigas Avenue Extension Corner St. Joseph, Brgy. Ro', NULL, '0000-00-00', '', NULL, 'No'),
(17, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-28', '22:00:00.000000', 'Thursday', 'Right Angle', 2, 'Night', 'Fair', 'Solved', 2, 26, 'ALONG MARCOS HIGHWAY AYALA FELIZ BRGY. SANTOLAN, PASIG CITY', '', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 44, 'Male', '', '', '', 'Sedan', '', '', '', NULL, '', NULL, NULL, '', 25, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, 'TYPE OF INCIDENT:\nReckless Imprudence Resulting in Damage to Property & Physical Injury (RIRI/DTP/PI) DATE/TIME OF INCIDENT:\nFebruary 28, 2019/ 2040H\nDATE/TIME OF RECORDED:\n     February 28, 2019/ 220', NULL, '0000-00-00', '', NULL, 'No'),
(18, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-28', '22:17:00.000000', 'Thursday', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 1, 12, 'ALONG DR. MALDO SINGER BRGY. SAGAD, PASIG CITY', '', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 36, 'Female', '', '', '', 'Sedan', '', '', '', NULL, '', NULL, NULL, '', 40, 'Male', '', '', '', 'Sedan', '', '', '', NULL, 'TYPE OF INCIDENT:\nReckless Imprudence Resulting in Damage to Property (RIRI/DTP) DATE/TIME OF INCIDENT:\nFebruary 28, 2019/ 2200H\nDATE/TIME OF RECORDED:\n     February 28, 2019/ 2217H   PLACE OF INCIDEN', NULL, '0000-00-00', '', NULL, 'No'),
(19, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-28', '22:45:00.000000', 'Thursday', 'Rear End Collision', 2, 'Night', 'Fair', 'Solved', 2, 20, 'ALONG MAGSAYSAY ST BRGY MANGGAHAN PASIG CITY', '', '', NULL, NULL, 'Dry', '', '', '', '', NULL, NULL, NULL, '', 35, 'Male', '', '', '', 'SUV', '', '', '', NULL, '', NULL, NULL, '', 0, '', '', '', '', '', '', '', '', NULL, 'TYPE OF INCIDENT:\nReckless Imprudence Resulting in Damage to Property (RIRI/DTP)  DATE/TIME OF INCIDENT:\nFebruary 28, 2019/ 2200H\nDATE/TIME OF REPORTED:\nFebruary 28,2019/ 2245H   PLACE OF INCIDENT:\nAl', NULL, '0000-00-00', '', NULL, 'No'),
(20, 'Pasig City', 'Pasig', 'Damage to Property', 4, '2021-08-08', '16:18:30.000000', 'Monday', 'sdfdsf', -12, 'dsfsd', 'dsfsd', 'dfd', 2, 6, '#115 60MM St., Soldiers Village, Sta. Lucia', 'dfd', 'df', NULL, NULL, 'ds', 'df', 'dsf', 'sdf', 'sdf', NULL, NULL, NULL, 'sdf', 11, 'sdf', 'dsf', 'fds', 'fsd', 'fdsf', 'sdfs', 'ds', 'fsdf', NULL, 'sdf', NULL, NULL, 'gjhj', 11, 'gjg', 'j', 'ghj', 'jh', 'j', 'g', 'ghj', 'jg', NULL, 'ghj', NULL, '2021-08-08', 'jgh', NULL, 'No'),
(21, 'Pasig', 'Pasig City Police Station', 'fdsfds', NULL, '2021-09-10', NULL, NULL, 'Hit and Run', 1, 'Day', 'Light Rain', 'Solved', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Wet', 'Concrete', 'Yes', 'Yes', 'Curve', NULL, NULL, NULL, 'Deceased', 20, 'Female', 'Widowed', 'sdsafas', 'Ewan', 'Cab Chassis ', '0323', 'dds', 'ssf', NULL, NULL, NULL, NULL, 'Harmed', 32, 'Male', 'Widowed', 'Unit 4G', 'Ewan', 'Sedan', '2332', 'fsfs', 'sds', NULL, 'fsfqqq', NULL, NULL, 'wala pa', NULL, 'No'),
(22, 'Pasig', 'Pasig City Police Station', 'Damage to Property', NULL, '2021-09-24', '16:16:00.000000', '', 'Self Accident', 1, 'Day', 'Rainy', 'Unsolved', 1, 6, NULL, NULL, NULL, NULL, NULL, 'Wet', 'Asphalt', 'No', 'No', 'Upwards', NULL, NULL, NULL, 'Identified', 12, 'Female', 'Widowed', 'dyan lang', 'Ewan', 'Hatchback', '0323', 'Tyrone', '', NULL, 'Driver', NULL, NULL, 'Identified', 22, 'Female', 'Single', '#115 60MM St., Soldiers Village, Sta. Lucia', 'Ewan', 'Coupe', 'PLY690', 'Jean', 'erwer', NULL, 'w', NULL, '2021-09-14', 'wala pa', NULL, 'No'),
(40, 'Pasig', 'Pasig City Police Station', 'HELO', 4, '2019-02-27', '15:20:00.000000', 'Thursday', 'Others', 2, 'hello', 'hello', 'Unsolved', 2, 21, 'hello', 'hello', 'hello', NULL, NULL, 'hello', 'hello', 'hello', 'hello', 'hello', NULL, NULL, NULL, 'hello', 12, 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', NULL, 'hello', NULL, NULL, 'hello', 14, 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', NULL, 'hello', NULL, '2021-09-14', NULL, NULL, 'No'),
(41, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 4, '2019-01-24', '15:20:00.000000', 'Thursday', 'Others', 2, 'Daylight', '', 'Solved', 2, 21, 'ALONG F LEGASPI ST BRGY MAYBUNGA PASIG CITY', '', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 23, '', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 34, 'Male', '', '', '', 'Tricycle', '', '', '', NULL, '', NULL, '2021-09-14', NULL, NULL, 'No'),
(42, 'Pasig', 'Pasig City Police Station', 'Damage to Property', NULL, '2021-09-04', '23:41:00.000000', '', 'Hit While Parked', 1, 'Day', 'Sun', 'Unsolved', 1, 2, NULL, NULL, NULL, NULL, NULL, '', 'Concrete', 'No', 'No', 'Straight Flat', NULL, NULL, NULL, 'Escaped', 21, 'Male', 'Married', 'Cainta', 'Ewan', 'S-CUV', '098TVG', 'Kim', '3435-234', NULL, 'Driver', NULL, NULL, 'Harmed', 23, 'Female', 'Single', 'Cack', 'Ewan', 'MTC/MC', 'PLY690', 'Mima', '22344-5566-dg', NULL, 'Hello', NULL, '2021-09-14', 'wala pa', NULL, 'Yes'),
(50, 'Pasig', 'Pasig City Police Station', '', NULL, '2021-09-08', '06:25:00.000000', '', 'Hit and Run', 1, 'Day', 'Rainy', 'Unsolved', 1, 10, NULL, NULL, NULL, NULL, NULL, 'Sand', 'Concrete', 'No', 'Yes', 'Curve', NULL, NULL, NULL, 'Identified', 23, 'Female', '', '#115 60MM St., Soldiers Village, Sta. Lucia', 'Ewan', 'Train', '098TVG', 'Dane1', '3435-dfddg', NULL, 'Driver', NULL, NULL, 'Harmed', 21, 'Male', 'Divorced', '#115 60MM St., Soldiers Village, Sta. Lucia', 'Ewan', 'Jitney', '2332', 'ghgfhgh', 'erwer', NULL, 'test .d/./sd.gsg!@#$@', NULL, '2021-09-15', 'wala pa', NULL, 'No'),
(51, 'Pasig', 'Pasig City Police Station', 'Damage to Property, Physical Injury', 6, '2019-02-06', '10:20:00.000000', 'Wednesday', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 2, 25, 'ALONG ORTIGAS AVE EXT BRGY STA LUCIA PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', 'Dry', '', '', '', NULL, NULL, NULL, '', 29, 'Male', '', '', '', 'Jitney', '', '', '', NULL, '', NULL, NULL, '', 18, 'Male', '', '', '', 'Bike', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(52, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 6, '2019-02-06', '19:30:00.000000', 'Wednesday', 'Others', 2, 'Night', '', 'Solved', 2, 24, 'ALONG C RAYMUNDO AVE COR MERCEDES AVE BRGY SAN MIGUEL PASIG CITY', 'C. Raymundo', 'Mercedes', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 40, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 37, 'Male', '', '', '', 'Tricycle', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(53, 'Pasig', 'Pasig City Police Station', 'Damage to Property, Physical Injury', 7, '2019-02-13', '23:15:00.000000', 'Wednesday', 'Sideswiped', 2, 'Night', 'Fair', 'Solved', 1, 1, 'ORTIGAS AVE COR PONTERA DRIVE BRGY UGONG PC', 'Ortigas Extension', '', NULL, NULL, '', 'Dry', '', '', '', NULL, NULL, NULL, '', 52, 'Male', '', '', '', 'Wagon', '', '', '', NULL, '', NULL, NULL, '', 29, 'Male', '', '', '', 'Truck', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(54, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 7, '2019-02-14', '20:40:00.000000', 'Thursday', 'Sideswiped', 2, 'Night', '', 'Solved', 2, 21, 'ALONG C RAYMUNDO AVE BRGY MAYBUNGA PASIG CITY', 'C. Raymundo', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 50, 'Female', '', '', '', 'SUV', '', '', '', NULL, '', NULL, NULL, '', 45, '', '', '', '', 'Sedan', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(55, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-24', '02:30:00.000000', 'Sunday', 'Rear End Collision', 2, 'Night', 'Fair', 'Solved', 2, 23, 'ALONG ORTIGAS AVENUE EXT BRGY ROSARIO PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', 'Dry', '', '', '', NULL, NULL, NULL, '', 41, 'Male', '', '', '', 'Wago', '', '', '', NULL, '', NULL, NULL, '', 21, '', '', '', '', 'Suv', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(56, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 9, '2019-02-27', '12:00:00.000000', 'Wednesday', 'Sideswiped', 2, 'Daylight', 'Fair', 'Solved', 1, 11, 'ALONG M.H DEL PILAR ST. BRGY PALATIW PASIG CITY', '', '', NULL, NULL, '', 'Dry', '', '', '', NULL, NULL, NULL, '', 24, 'Male', '', '', '', 'Sedan', '', '', '', NULL, '', NULL, NULL, '', 28, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'No'),
(57, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-27', '13:30:00.000000', 'Wednesday', 'Rear End Collision', 2, 'Daylight', '', 'Solved', 1, 1, 'ALONG ORTIGAS AVENUE WESTBOUND UGONG, PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 22, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, '', NULL, NULL, '', 78, '', '', '', '', 'Unidentified', '', '', '', NULL, NULL, NULL, '2021-09-15', NULL, NULL, 'Yes'),
(58, 'Pasig1', 'Pasig City Police Station', 'Physical Injury', 9, '2019-02-27', '13:30:00.000000', 'Wednesday', 'Rear End Collision', 2, 'Daylight', '', 'Solved', 1, 1, 'ALONG ORTIGAS AVENUE WESTBOUND UGONG, PASIG CITY', 'Ortigas Extension', '', NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, '', 22, 'Male', '', '', '', 'Motorcycle', '', '', '', NULL, '', NULL, NULL, '', 56, '', '', '', '', 'Unidentified', '', '', '', NULL, NULL, 8, '2021-09-15', NULL, NULL, 'No'),
(70, 'Pasig', 'Pasig City Police Station', 'Physical Injury', NULL, '2021-09-21', '19:31:00.000000', NULL, '', 1, 'Day', '', 'Unsolved', 1, 4, 'Village', NULL, NULL, NULL, NULL, '', '', '', '', '', NULL, NULL, NULL, 'Deceased', 21, 'Male', 'Single', 'Riverside Compound', 'Model1', 'PUJ - Public Utility Jeep', '098TVG', 'Dane Malolos', '3435-234', NULL, '', NULL, NULL, '', 78, '', '', '', '', '', '', '', '', NULL, '', 11, '2021-09-24', 'wala pa', NULL, 'No'),
(71, 'Pasig', 'Pasig City Police Station', 'Physical Injury', NULL, '2021-09-21', '19:31:00.000000', NULL, 'Self Accident', 1, 'Day', 'Fair', 'Solved', NULL, 4, 'Village', NULL, NULL, NULL, NULL, 'Wet', 'Asphalt', 'No', 'No', 'Downwards', NULL, NULL, NULL, 'Deceased', 21, 'Male', 'Single', 'Riverside Compound', 'Model1', 'PUJ - Public Utility Jeep', '098TVG', 'Dane Malolos', '3435-234', NULL, 'Driver', NULL, NULL, 'Unharmed', 21, 'Male', 'Single', 'Angono, Rizal', 'Model2', 'Electric Bike', 'PLY690', 'Jc Agaton', '22344-5566-dg', NULL, 'Hmm', 9, '2021-09-24', 'wala pa', NULL, 'Yes'),
(72, 'Pasig', 'Pasig', 'Physical Injury', 2, '2021-09-25', '16:25:51.000000', 'Monday', 'Hit Object Off Road', 2, 'Daylight', 'Fair', 'Solved', 1, 16, '#115 60MM St., Soldiers Village, Sta. Lucia', 'Along', 'Cornerrr', NULL, NULL, 'Dry', 'Concrete', 'No', 'No', 'Curve', 'Passenger', NULL, NULL, 'Unharmed', 21, 'Female', 'Widowed', '#115 60MM St., Soldiers Village, Sta. Lucia', 'Honda', 'Hatchback', '123-321', 'Karen Faith', 'QWE-321', '2021-09-25', 'Passenger', NULL, NULL, 'Harmed', 11, 'Female', 'Widowed', 'Unit 2k', 'Model2ddd', 'Sedan', 'POL-097', 'Karen Faith Abuan', '9679-543-RED', '2021-09-25', 'This case is solved.', 5, '2021-09-25', 'Admin', 'No', 'No'),
(73, 'Pasig', 'Pasig City Police Station', 'Self Accident', NULL, '2021-09-08', '16:51:00.000000', 'Wednesday', 'Bumped From Behind', 1, 'Day', 'Fair', 'Solved', 1, 2, 'Village', 'Kaliwa', 'Kanan', NULL, NULL, 'Wet', 'Asphalt', 'No', 'No', 'Straight Flat', '', NULL, NULL, '', 89, 'Male', '', '#115 60MM St., Soldiers Village, Sta. Lucia', '', '', '', '', '', '2021-09-07', '', NULL, NULL, '', 21, 'Male', '', '', '', '', '', '', '', NULL, '', 11, '2021-09-25', 'wala pa', 'No', 'No'),
(74, 'Pasig', 'Pasig City Police Station', 'Physical Injury,Damage to Property', NULL, '2021-09-08', '23:32:00.000000', 'Wednesday', 'Right Angle', 1, 'Day', 'Light Rain', 'Solved', 1, 30, 'Marikina Sub', 'Kaliwa', 'Kanan', NULL, NULL, 'Sand', 'Soil', 'No', 'Yes', 'Curve', 'Passenger', 'KAREN', 'ABUAN', 'Injured', 34, 'Female', 'Married', '#115 60MM St., Soldiers Village, Sta. Lucia', 'None13', 'Shuttle', 'OMWTFYB', 'KAREN ABUAN', '3435-234', '2021-09-08', 'Pedestrian', 'Kim Joel', 'Abuan', 'Arrested', 43, 'Male', 'Married', 'Unit 2k', 'None111', 'Hatchback', 'PLY690', 'Kim Joel Abuan', '987-654-321', NULL, 'eeee', 9, '2021-09-25', 'For now encoder', 'No', 'No'),
(75, 'Pasig', 'Pasig City Police Station', 'Physical Injury,Damage to Property', 37, '2021-09-08', '23:32:00.000000', 'Wednesday', 'Right Angle', 1, 'Day', 'Light Rain', 'Solved', NULL, 30, 'Marikina Sub', 'Kaliwa', 'Kanan', NULL, NULL, 'Sand', 'Soil', 'No', 'Yes', 'Curve', 'Passenger', 'KAREN', 'ABUAN', 'Injured', 34, 'Female', 'Married', '#115 60MM St., Soldiers Village, Sta. Lucia', 'None13', 'Shuttle', 'OMWTFYB', 'KAREN ABUAN', '3435-234', '2021-09-08', 'Pedestrian', 'Kim Joel', 'Abuan', 'Arrested', 43, 'Male', 'Married', 'Unit 2k', 'None111', 'Hatchback', 'PLY690', 'Kim Joel Abuan', '987-654-321', NULL, 'eeee', 8, '2021-09-25', 'For now encoder', 'No', 'No'),
(76, 'Pasig', 'Pasig City Police Station', NULL, 37, '2021-09-14', '12:54:00.000000', '', 'Right Angle', 1, 'Day', 'Light Rain', 'Solved', 1, 18, 'Village', 'Kaliwa', 'Kanan', NULL, NULL, 'Dry', 'Asphalt', 'No', 'Yes', 'Curve Incline', 'Passenger', 'Kim Joela', 'Abuana', 'Unharmed', 43, 'Male', 'Widowed', 'Unit 2k', 'Model1', 'Pedicab', 'OMWTFYB', 'Kim Joela Abuan', '3435-234', '2021-09-02', 'Passenger', 'Kim Joela', 'Abuana', 'Arrested', 543, 'Male', 'Widowed', 'Village', 'Model2', 'Pedicab', 'PLY6901', 'Kim Joel Abuan', '987-654-321', '2021-09-19', '                                                                                                                                                                                                    L                                                                                                                                                                                                                                                                                                                                                                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis au\r\n                        ', 11, '2021-09-26', 'For now encoder', 'No', 'No'),
(77, 'Pasig', 'Pasig City Police Station', '', 36, '2021-09-07', '14:24:00.000000', 'Tuesday', 'Rear End', 1, 'Day', 'Rainy', '', 1, 12, '', '', '', NULL, NULL, '', '', '', '', '', '', '', '', '', 21, '', '', '', '', '', '', '', '', '2021-09-22', '', '', '', '', 23, '', '', '', '', '', '', '', '', '2021-09-21', '', 8, '2021-09-26', 'For now encoder', 'No', 'No'),
(78, 'Pasig', 'Pasig City Police Station', 'Damage to Property', NULL, NULL, NULL, NULL, NULL, 1, 'Day', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 28, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2021-09-28', 'For now encoder', 'No', 'No'),
(79, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 37, '2021-09-10', '09:36:00.000000', 'Friday', '', 1, 'Day', '', 'Unsolved', NULL, 7, '', '', '', NULL, NULL, '', '', '', '', '', '', '', '', '', 39, '', '', '', '', '', '', '', '', '2021-09-16', '', '', '', '', 83, '', '', '', '', '', '', '', '', '2021-09-07', '', 9, '2021-09-28', 'For now encoder', 'No', 'No'),
(80, 'Pasig', 'Pasig City Police Station', 'Physical Injury,Damage to Property', 37, '2021-09-09', '10:11:00.000000', 'Thursday', 'Side Impact', 1, 'Day', 'Wind', 'Solved', 1, 12, 'Anne Claire Montessori, Santo Niño Street, Taguig, Metro Manila, Philippines', '', '', NULL, NULL, 'Dry', 'Concrete', 'No', 'No', 'Curve', '', '', '', '', 45, '', '', '', '', '', '', '', '', '2021-10-25', '', '', '', '', 19, '', '', '', '', '', '', '', '', '2021-09-28', 'sup', 9, '2021-09-30', 'For now encoder', 'No', 'No'),
(81, 'Pasig', 'Pasig City Police Station', '', 37, '2021-09-08', '10:31:00.000000', 'Wednesday', '', 1, 'Day', '', 'Unsolved', NULL, 17, '', '', '', '14.5614557', '121.0829526', '', '', '', '', '', '', '', '', '', 59, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 49, '', '', '', '', '', '', '', '', '2021-09-05', '', 9, '2021-09-30', 'For now encoder', 'No', 'Yes'),
(82, 'Pasig', 'Pasig City Police Station', '', 37, '2021-09-08', '10:31:00.000000', 'Wednesday', '', 1, 'Day', '', 'Unsolved', NULL, 17, '', '', '', '14.5614557', '121.0829526', '', '', '', '', '', '', '', '', '', 33, '', '', '', '', '', '', '', '', '2021-09-14', '', '', '', '', 51, '', '', '', '', '', '', '', '', '2021-09-05', '', 9, '2021-09-30', 'For now encoder', 'No', 'No'),
(83, 'Pasig', 'Pasig City Police Station', 'Self Accident', 38, '2021-09-20', '10:34:00.000000', 'Monday', '', 1, 'Day', '', 'Unsolved', 1, 12, 'Greenwoods Executive Village - Pasig Gate, Greenwoods Avenue, Pasig, Metro Manila, Philippines', '', '', '14.5619981', '121.0965925', '', '', '', '', '', '', 'KAREN', 'ABUAN', '', 60, '', '', '#115 60MM St., Soldiers Village, Sta. Lucia', '', '', '', 'KAREN ABUAN', '', NULL, '', 'Kim Joel', 'Abuan', '', 62, '', '', 'Unit 2k', '', '', '', 'Kim Joel Abuan', '', NULL, 'hjhj', 8, '2021-09-30', 'For now encoder', 'No', 'Yes'),
(84, 'Pasig', 'Pasig City Police Station', 'Self Accident', 38, '2021-09-20', '10:34:00.000000', 'Monday', '', 1, 'Day', '', 'Unsolved', NULL, 12, '', '', '', '14.5619981', '121.0965925', '', '', '', '', '', '', 'KAREN', 'ABUAN', '', 63, '', '', '#115 60MM St., Soldiers Village, Sta. Lucia', '', '', '', 'KAREN ABUAN', '', NULL, '', 'Kim Joel', 'Abuan', '', 52, '', '', 'Unit 2k', '', '', '', 'Kim Joel Abuan', '', NULL, 'hjhj', 8, '2021-09-30', 'For now encoder', 'No', 'No'),
(85, 'Pasig', 'Pasig City Police Station', 'Self Accident', 38, '2021-09-20', '10:34:00.000000', 'Monday', '', 1, 'Day', '', 'Unsolved', NULL, 12, '', '', '', '14.5619981', '121.0965925', '', '', '', '', '', '', 'KAREN', 'ABUAN', '', 89, '', '', '#115 60MM St., Soldiers Village, Sta. Lucia', '', '', '', 'KAREN ABUAN', '', NULL, '', 'Kim Joel', 'Abuan', '', 20, '', '', 'Unit 2k', '', '', '', 'Kim Joel Abuan', '', NULL, 'hjhj', 8, '2021-09-30', 'For now encoder', 'No', 'No'),
(86, 'Pasig', 'Pasig City Police Station', 'Homicide', 38, '2021-09-21', '10:46:00.000000', 'Tuesday', 'Head On', 1, 'Day', 'Light Rain', 'Solved', 1, 17, 'Palengke, R. Jabson Street, Pateros, Metro Manila, Philippines', 'Row 1', 'Row 2', '14.551334', '121.0745793', 'Wet', 'Soil', 'Yes', 'Yes', 'Straight Incline', '', '', '', '', 36, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 69, '', '', '', '', '', '', '', '', NULL, '', 11, '2021-09-30', 'For now encoder', 'No', 'Yes'),
(87, 'Pasig', 'Pasig City Police Station', 'Physical Injury', 42, '2021-10-14', '10:37:00.000000', 'Thursday', 'Clash', 1, 'Day', 'Sun', 'Solved', 1, 7, 'Pasig City General Hospital, Eusebio, Pasig, Metro Manila, Philippines', 'Meralco Ave.', 'Ministop', '14.5721964', '121.0994306', 'Wet', 'Asphalt', 'No', 'No', 'Curve', 'Driver', 'Kim', 'Tan', 'Unharmed', 18, 'Male', 'Single', 'Tower', 'Model1', 'Train', 'OMWTFYB', 'Kim Tan', '3435-234', '2021-10-06', 'Passenger', 'Eun', 'Sang', 'Unharmed', 18, 'Female', 'Single', 'Room 1', 'Model2', 'Bicycle', 'PLY690', 'Eun Sang', '987-654-321', NULL, 'October Test :)', 5, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(88, 'Pasig', 'Pasig City Police Station', '', 40, '2021-10-01', '11:10:00.000000', '', 'Damage to Property', 1, 'Day', 'Sun', 'Solved', 2, 20, 'Soldiers Village Covered Court, Pasig, Metro Manila, Philippines', '', '', '14.5773325', '121.1023017', 'Dry', 'Asphalt', 'Yes', 'Yes', 'Curve', 'Passenger', 'Kim ', 'Tan', '', 17, 'Male', 'Married', '#', '', '', '', 'Kim  Tan', '', NULL, 'Driver', 'Yeong', 'Do', '', 18, 'Male', 'Married', 'Soldiers Village Covered Court, Pasig, Metro Manila, Philippines', '', '', '', 'Yeong Do', '', NULL, '', 5, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(89, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 40, '2021-10-01', '11:13:00.000000', 'Friday', 'Hit Animals', 1, 'Day', 'Wind', 'Solved', 1, 15, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 48, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 24, '', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'No'),
(90, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 40, '2021-09-30', '11:13:00.000000', 'Thursday', 'Hit Animals', 1, 'Day', 'Wind', 'Solved', NULL, 15, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 28, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 41, '', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'No'),
(91, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 40, '2021-09-30', '11:13:00.000000', 'Thursday', 'Hit Animals', 1, 'Day', 'Wind', 'Solved', NULL, 15, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 16, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 28, '', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'No'),
(92, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 39, '2021-09-26', '11:13:00.000000', 'Sunday', 'Hit Animals', 1, 'Day', 'Wind', 'Solved', NULL, 15, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 32, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 36, '', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'No'),
(93, 'Pasig', 'Pasig City Police Station', 'Damage to Property', 39, '2021-09-27', '11:13:00.000000', 'Monday', 'Hit Animals', 1, 'Day', 'Wind', 'Solved', NULL, 15, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 27, '', '', '', '', '', '', '', '', NULL, '', '', '', '', 53, '', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(94, 'Pasig', 'Pasig City Police Station', '', 41, '2021-10-02', '11:13:00.000000', '', 'Hit Animals', 1, 'Day', '', 'Solved', 1, 15, 'karangalan', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 45, 'Female', '', '', '', '', '', '', '', NULL, '', '', '', '', 23, 'Male', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(95, 'Pasig', 'Pasig City Police Station', 'Self Accident', 40, '2021-10-03', '11:13:00.000000', '', 'Hit Animals', 1, 'Day', '', 'Solved', 1, 13, 'market', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 34, 'Male', '', '', '', '', '', '', '', NULL, '', '', '', '', 51, 'Female', '', 'market', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(96, 'Pasig', 'Pasig City Police Station', '', 40, '2021-10-04', '11:13:00.000000', '', 'Hit Animals', 1, 'Day', '', 'Solved', 1, 5, '', '', '', '', '', 'Dry', 'Asphalt', '', '', 'Straight Incline', '', '', '', '', 25, 'Female', '', '', '', '', '', '', '', NULL, '', '', '', '', 4, 'Male', '', '', '', '', '', '', '', NULL, '', 9, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(97, 'Pasig', 'Pasig City Police Station', '', 39, '2021-10-01', '12:32:00.000000', '', '', 1, 'Day', '', 'Unsolved', 1, 15, 'Cambridge Village, Cambridge Street, Cainta, Rizal, Philippines', '', '', '14.5701388', '121.1082533', '', '', '', '', '', '', '', '', '', 13, 'Male', '', '', '', '', '', '', '', '2021-09-28', '', '', '', '', 57, 'Female', '', 'Pasig Rainforest Park, Francisco Legaspi, Pasig, Metro Manila, Philippines', '', '', '', '', '', '2021-09-28', '', 5, '2021-10-01', 'For now encoder', 'No', 'Yes'),
(98, 'Pasig', 'Pasig City Police Station', '', 40, '2021-10-06', '21:40:00.000000', 'Wednesday', '', 1, 'Day', '', 'Unsolved', 1, 15, 'Market Avenue, Pasig, Metro Manila, Philippines', '', '', '14.5627711', '121.0847004', '', '', '', '', '', '', '', '', '', 21, 'Female', '', '', '', '', '', '', '', NULL, '', '', '', '', 74, 'Male', '', '', '', '', '', '', '', NULL, '', 5, '2021-10-02', 'For now encoder', 'No', 'Yes'),
(99, 'Pasig', 'Pasig City Police Station', '', 40, '2020-11-12', '21:40:00.000000', '', '', 1, 'Day', '', 'Unsolved', 2, 22, 'Pasig Rainforest Park, Francisco Legaspi, Pasig, Metro Manila, Philippines', '', '', '14.5738401', '121.0976382', '', '', '', '', '', '', '', '', '', 21, 'Female', '', '', '', '', '', '', '', NULL, '', '', '', '', 74, 'Male', '', 'Pasig Rainforest Park, Francisco Legaspi, Pasig, Metro Manila, Philippines', '', '', '', '', '', NULL, '', 5, '2021-10-02', 'For now encoder', 'No', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_position`
--

CREATE TABLE `roadcast_tbl_position` (
  `id` bigint(20) NOT NULL,
  `Position` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_position`
--

INSERT INTO `roadcast_tbl_position` (`id`, `Position`) VALUES
(3, 'NUP'),
(4, 'Pat'),
(5, 'PCpl'),
(6, 'PSSg'),
(7, 'PMGSg'),
(8, 'PSMSg'),
(10, 'PCMSg'),
(11, 'PEMSg'),
(12, 'PLT'),
(13, 'PCAP'),
(14, 'PMAJ'),
(15, 'PLTCOL'),
(16, 'PCOL'),
(17, 'PBGEN'),
(18, 'PMGEN'),
(19, 'PLTGEN'),
(20, 'PGEN');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_public_report`
--

CREATE TABLE `roadcast_tbl_public_report` (
  `id` bigint(20) NOT NULL,
  `User_ID_id` bigint(20) DEFAULT NULL,
  `Reported_City` varchar(200) NOT NULL,
  `Reported_District` varchar(200) NOT NULL,
  `Reported_Location` varchar(200) NOT NULL,
  `Reported_Along` varchar(200) NOT NULL,
  `Reported_Corner` varchar(200) NOT NULL,
  `Reported_Narrative` varchar(800) NOT NULL,
  `Reported_Image_Proof` varchar(100) NOT NULL,
  `Reported_Date` date NOT NULL,
  `Reported_Time` time(6) NOT NULL,
  `Recipient` varchar(200) NOT NULL,
  `Read_Status` varchar(200) NOT NULL,
  `Report_Status` varchar(200) NOT NULL,
  `Assigned_Investigator_id` int(11) DEFAULT NULL,
  `Reported_Brgy_id` bigint(20) DEFAULT NULL,
  `Substation_id` bigint(20) DEFAULT NULL,
  `Reported_Latitude` varchar(200) NOT NULL,
  `Reported_Longitude` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_public_report`
--

INSERT INTO `roadcast_tbl_public_report` (`id`, `User_ID_id`, `Reported_City`, `Reported_District`, `Reported_Location`, `Reported_Along`, `Reported_Corner`, `Reported_Narrative`, `Reported_Image_Proof`, `Reported_Date`, `Reported_Time`, `Recipient`, `Read_Status`, `Report_Status`, `Assigned_Investigator_id`, `Reported_Brgy_id`, `Substation_id`, `Reported_Latitude`, `Reported_Longitude`) VALUES
(11, 1, 'Pasig', '1', '#2 Sesame Street', '', '', 'Hello', 'incident_images/2021-10-2021-10-04_130751.9246090000-Caniogan-PasigCapture-MC0IfhkIso.PNG', '2021-10-04', '13:07:51.924609', 'Admin', 'Yes', 'Unsolved', NULL, 4, NULL, '', ''),
(12, 1, 'Pasig', '1', '#12 Baker St.', '', '', 'Mamama', 'incident_images/2021-10-2021-10-04_130751.9246090000-Santa_Cruz-Pasigmilktea-x7M0COpHZh.png', '2021-10-04', '13:07:51.924609', 'Admin', 'Yes', 'Unsolved', NULL, 29, NULL, '', ''),
(13, 2, 'Pasig', '1', '#19 Honeymoon Avenue', '', '', 'yeyee', 'incident_images/2021-10-2021-10-04_130751.9246090000-Bagong_Ilog-PasigDSA-Rpxlx7UnY8.PNG', '2021-10-04', '13:07:51.924609', 'Admin', 'Yes', 'Unsolved', 5, 2, 1, '', ''),
(14, 1, 'Pasig', '1', '#21 Palatiw', 'Meralco Ave.', 'Tricycle Terminal', 'Red light, green light', 'incident_images/2021-10-2021-10-06_053712.2173960000-Palatiw-PasigCapture-l4QFheil02.PNG', '2021-10-06', '05:37:12.217396', 'Admin', 'No', 'Unsolved', NULL, 11, NULL, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_public_report_response`
--

CREATE TABLE `roadcast_tbl_public_report_response` (
  `Response_id` int(11) NOT NULL,
  `Response` varchar(200) DEFAULT NULL,
  `Response_Date` date DEFAULT NULL,
  `Sender` int(11) DEFAULT NULL,
  `Receiver` int(11) DEFAULT NULL,
  `Report_id` bigint(20) DEFAULT NULL,
  `Response_Time` time(6) DEFAULT NULL,
  `Read_Status` varchar(200) DEFAULT NULL,
  `Sender_Type` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_public_report_response`
--

INSERT INTO `roadcast_tbl_public_report_response` (`Response_id`, `Response`, `Response_Date`, `Sender`, `Receiver`, `Report_id`, `Response_Time`, `Read_Status`, `Sender_Type`) VALUES
(2, 'Noted with thanks!', '2021-10-05', 4, 2, 13, '14:29:33.948125', 'No', 'Admin'),
(3, 'Patrol group is on their way. Thank you', '2021-10-05', 4, 1, 12, '14:29:33.948125', 'No', 'Admin'),
(4, 'Please wait for their arrival.', '2021-10-05', 4, 1, 12, '14:43:14.328605', 'No', 'Admin'),
(14, 'Noted po!', '2021-10-06', 1, 4, 12, '14:48:27.031829', 'No', 'Public'),
(15, 'Oki', '2021-10-06', 4, 1, 12, '14:48:27.031829', 'No', 'Admin'),
(16, 'ssss', '2021-10-06', 4, 2, 13, '14:48:27.031829', 'No', 'Admin'),
(17, 'Okay poo', '2021-10-06', 2, 4, 13, '14:48:27.031829', 'No', 'Public');

-- --------------------------------------------------------

--
-- Table structure for table `roadcast_tbl_substation`
--

CREATE TABLE `roadcast_tbl_substation` (
  `id` bigint(20) NOT NULL,
  `Substation` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roadcast_tbl_substation`
--

INSERT INTO `roadcast_tbl_substation` (`id`, `Substation`) VALUES
(1, 'Substation 1'),
(2, 'Substation 2'),
(3, 'Substation 3'),
(4, 'Substation 4'),
(5, 'Substation 5'),
(6, 'Substation 6'),
(7, 'Substation 7'),
(8, 'Substation 8');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `roadcast_tbl_add_departments`
--
ALTER TABLE `roadcast_tbl_add_departments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_add_members`
--
ALTER TABLE `roadcast_tbl_add_members`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roadcast_tbl_add_mem_Members_Position_id_23201946_fk_roadcast_` (`Members_Position_id`),
  ADD KEY `roadcast_tbl_add_mem_Members_Substation_i_1888d946_fk_roadcast_` (`Members_Substation_id`),
  ADD KEY `roadcast_tbl_add_mem_Members_User_id_771454ef_fk_roadcast_` (`Members_User_id`),
  ADD KEY `roadcast_tbl_add_mem_Members_Dept_id_ed483bc0_fk_roadcast_` (`Members_Dept_id`);

--
-- Indexes for table `roadcast_tbl_audit`
--
ALTER TABLE `roadcast_tbl_audit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_barangay`
--
ALTER TABLE `roadcast_tbl_barangay`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roadcast_tbl_baranga_District_id_id_5a7f2be0_fk_roadcast_` (`District_id_id`);

--
-- Indexes for table `roadcast_tbl_district`
--
ALTER TABLE `roadcast_tbl_district`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_forecast`
--
ALTER TABLE `roadcast_tbl_forecast`
  ADD PRIMARY KEY (`Date`);

--
-- Indexes for table `roadcast_tbl_genpub_users`
--
ALTER TABLE `roadcast_tbl_genpub_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_member_type`
--
ALTER TABLE `roadcast_tbl_member_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_pasig_incidents`
--
ALTER TABLE `roadcast_tbl_pasig_incidents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roadcast_tbl_pasig_i_Barangay_id_id_8076f1fe_fk_roadcast_` (`Barangay_id_id`),
  ADD KEY `roadcast_tbl_pasig_i_District_id_693f55f8_fk_roadcast_` (`District_id`),
  ADD KEY `roadcast_tbl_pasig_incidents_Investigator_id_a3d001e1` (`Investigator_id`);

--
-- Indexes for table `roadcast_tbl_position`
--
ALTER TABLE `roadcast_tbl_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roadcast_tbl_public_report`
--
ALTER TABLE `roadcast_tbl_public_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roadcast_tbl_public__Reported_Brgy_id_ff72f606_fk_roadcast_` (`Reported_Brgy_id`),
  ADD KEY `roadcast_tbl_public__Substation_id_459c65d6_fk_roadcast_` (`Substation_id`),
  ADD KEY `roadcast_tbl_public_report_Assigned_Investigator_id_f32677d5` (`Assigned_Investigator_id`),
  ADD KEY `roadcast_tbl_public_report_User_ID_id_fdf2ea18` (`User_ID_id`);

--
-- Indexes for table `roadcast_tbl_public_report_response`
--
ALTER TABLE `roadcast_tbl_public_report_response`
  ADD PRIMARY KEY (`Response_id`),
  ADD KEY `roadcast_tbl_public__Report_id_c0fe0c7d_fk_roadcast_` (`Report_id`);

--
-- Indexes for table `roadcast_tbl_substation`
--
ALTER TABLE `roadcast_tbl_substation`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `roadcast_tbl_add_departments`
--
ALTER TABLE `roadcast_tbl_add_departments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `roadcast_tbl_add_members`
--
ALTER TABLE `roadcast_tbl_add_members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `roadcast_tbl_audit`
--
ALTER TABLE `roadcast_tbl_audit`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `roadcast_tbl_barangay`
--
ALTER TABLE `roadcast_tbl_barangay`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `roadcast_tbl_district`
--
ALTER TABLE `roadcast_tbl_district`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `roadcast_tbl_genpub_users`
--
ALTER TABLE `roadcast_tbl_genpub_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `roadcast_tbl_member_type`
--
ALTER TABLE `roadcast_tbl_member_type`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `roadcast_tbl_pasig_incidents`
--
ALTER TABLE `roadcast_tbl_pasig_incidents`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `roadcast_tbl_position`
--
ALTER TABLE `roadcast_tbl_position`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `roadcast_tbl_public_report`
--
ALTER TABLE `roadcast_tbl_public_report`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `roadcast_tbl_public_report_response`
--
ALTER TABLE `roadcast_tbl_public_report_response`
  MODIFY `Response_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `roadcast_tbl_substation`
--
ALTER TABLE `roadcast_tbl_substation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `roadcast_tbl_add_members`
--
ALTER TABLE `roadcast_tbl_add_members`
  ADD CONSTRAINT `roadcast_tbl_add_mem_Members_Dept_id_ed483bc0_fk_roadcast_` FOREIGN KEY (`Members_Dept_id`) REFERENCES `roadcast_tbl_add_departments` (`id`),
  ADD CONSTRAINT `roadcast_tbl_add_mem_Members_Position_id_23201946_fk_roadcast_` FOREIGN KEY (`Members_Position_id`) REFERENCES `roadcast_tbl_position` (`id`),
  ADD CONSTRAINT `roadcast_tbl_add_mem_Members_Substation_i_1888d946_fk_roadcast_` FOREIGN KEY (`Members_Substation_id`) REFERENCES `roadcast_tbl_substation` (`id`),
  ADD CONSTRAINT `roadcast_tbl_add_mem_Members_User_id_771454ef_fk_roadcast_` FOREIGN KEY (`Members_User_id`) REFERENCES `roadcast_tbl_member_type` (`id`);

--
-- Constraints for table `roadcast_tbl_barangay`
--
ALTER TABLE `roadcast_tbl_barangay`
  ADD CONSTRAINT `roadcast_tbl_baranga_District_id_id_5a7f2be0_fk_roadcast_` FOREIGN KEY (`District_id_id`) REFERENCES `roadcast_tbl_district` (`id`);

--
-- Constraints for table `roadcast_tbl_pasig_incidents`
--
ALTER TABLE `roadcast_tbl_pasig_incidents`
  ADD CONSTRAINT `roadcast_tbl_pasig_i_Barangay_id_id_8076f1fe_fk_roadcast_` FOREIGN KEY (`Barangay_id_id`) REFERENCES `roadcast_tbl_barangay` (`id`),
  ADD CONSTRAINT `roadcast_tbl_pasig_i_District_id_693f55f8_fk_roadcast_` FOREIGN KEY (`District_id`) REFERENCES `roadcast_tbl_district` (`id`),
  ADD CONSTRAINT `roadcast_tbl_pasig_i_Investigator_id_a3d001e1_fk_roadcast_` FOREIGN KEY (`Investigator_id`) REFERENCES `roadcast_tbl_add_members` (`id`);

--
-- Constraints for table `roadcast_tbl_public_report`
--
ALTER TABLE `roadcast_tbl_public_report`
  ADD CONSTRAINT `roadcast_tbl_public__Assigned_Investigato_f32677d5_fk_roadcast_` FOREIGN KEY (`Assigned_Investigator_id`) REFERENCES `roadcast_tbl_add_members` (`id`),
  ADD CONSTRAINT `roadcast_tbl_public__Reported_Brgy_id_ff72f606_fk_roadcast_` FOREIGN KEY (`Reported_Brgy_id`) REFERENCES `roadcast_tbl_barangay` (`id`),
  ADD CONSTRAINT `roadcast_tbl_public__Substation_id_459c65d6_fk_roadcast_` FOREIGN KEY (`Substation_id`) REFERENCES `roadcast_tbl_substation` (`id`),
  ADD CONSTRAINT `roadcast_tbl_public__User_ID_id_fdf2ea18_fk_roadcast_` FOREIGN KEY (`User_ID_id`) REFERENCES `roadcast_tbl_genpub_users` (`id`);

--
-- Constraints for table `roadcast_tbl_public_report_response`
--
ALTER TABLE `roadcast_tbl_public_report_response`
  ADD CONSTRAINT `roadcast_tbl_public__Report_id_c0fe0c7d_fk_roadcast_` FOREIGN KEY (`Report_id`) REFERENCES `roadcast_tbl_public_report` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
