-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2024 at 09:52 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `url_shortener`
--

-- --------------------------------------------------------

--
-- Table structure for table `links`
--

CREATE TABLE `links` (
  `email` varchar(50) NOT NULL,
  `original_URL` varchar(100) NOT NULL,
  `short_URL` varchar(50) NOT NULL,
  `clicks` int(11) NOT NULL,
  `expiration` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `links`
--

INSERT INTO `links` (`email`, `original_URL`, `short_URL`, `clicks`, `expiration`) VALUES
('mashi@gmail.com', 'https://www.youtube.com/', 'http://short.url/9T60Of', 1, NULL),
('mashi@gmail.com', 'https://questionary.readthedocs.io/en/stable/pages/advanced.html', 'http://short.url/Df32MZ', 2, '2024-01-26'),
('mashi@gmail.com', 'https://www.google.com/', 'http://short.url/ocF6S9', 0, '2023-01-23');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`name`, `email`, `password`) VALUES
('mashi', 'mashi@gmail.com', '$2b$12$oKQgDo2ZtsXOxHNOKNkKgO6FEoUSvIHGrxb2anakVc095bdj4uXIe'),
('Rando', 'rando@gmail.com', '$2b$12$NGvEMYo0kSc.Wp1iU9skruzRsChssI3klS2FxvBt.VFXaavAH7/BO');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `links`
--
ALTER TABLE `links`
  ADD PRIMARY KEY (`short_URL`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
