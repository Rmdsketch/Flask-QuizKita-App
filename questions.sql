-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jan 2024 pada 18.54
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizkita`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `questions`
--

CREATE TABLE `questions` (
  `q_id` int(11) NOT NULL,
  `ques` varchar(350) DEFAULT NULL,
  `a` varchar(100) DEFAULT NULL,
  `b` varchar(100) DEFAULT NULL,
  `c` varchar(100) DEFAULT NULL,
  `d` varchar(100) DEFAULT NULL,
  `ans` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `questions`
--

INSERT INTO `questions` (`q_id`, `ques`, `a`, `b`, `c`, `d`, `ans`) VALUES
(1, 'Kerangka kerja Flask biasanya ditulis dalam bahasa apa?\r\n\r\n', 'Java', 'Python', 'JavaScrip', 'Ruby', 'Python'),
(2, 'Siapa orang pertama yang mengembangkan Flask?\r\n\r\n', 'Guido van Rossum', 'Krisna Balaram', 'James Gosling', 'Armin Ronacher', 'Armin Ronacher'),
(3, 'Flask adalah sebuah kerangka kerja untuk?\r\n\r\n', 'Pengembangan web', 'Pengembangan basis data', 'Pengembangan cloud', 'Pengembangan seluler', 'Pengembangan web'),
(4, 'Apakah framework Flask bersifat open source?', 'Benar', 'Salah', 'Mungkin benar atau salah', 'Tidak didefinisikan', 'Benar'),
(5, 'Bagaimana cara menambahkan fitur mailing di Aplikasi Flask?', 'pip install Flask', 'pip install Flask-Mail', 'install Flask-Mail', 'pip Flask-Mail', ' pip install Flask-Mail'),
(6, 'Port default Flask adalah?', '2000', '3000', '4000', '5000', '5000'),
(7, 'Formulir di Flask dapat diimplementasikan dengan menggunakan ekstensi yang disebut ?', 'Flask-ATF', 'Flask-WTF', 'Flask-GTM', 'Flask-ZIP', 'Flask-WTF'),
(8, 'Flask berfungsi dengan sebagian besar RDBMS, seperti?', 'PostgreSQL', 'SQLite', 'MySQL', 'Semua pilihan di atas benar', 'Semua pilihan diatas benar'),
(9, 'Apa yang dimaksud dengan WSGI Web Server Gateway Interface (WSGI) dalam Flask?', 'Wide System Gateway Interface', 'Web Server Gateway Interface', 'Web System Gateway Interface', 'Wide Server Gateway Interface', 'Web Server Gateway Interface'),
(10, 'function dari kelas Flask adalah sebuah dekorator yang menginstruksikan aplikasi untuk memanggil fungsi terkait?', 'Route()', 'Api()', 'Name()', 'Semua Benar', 'Route()');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`q_id`),
  ADD UNIQUE KEY `ques` (`ques`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `q_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
