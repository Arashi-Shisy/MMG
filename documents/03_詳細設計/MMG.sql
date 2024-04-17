CREATE TABLE `users` (
  `user_id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(256) NOT NULL,
  `del_flg` int NOT NULL DEFAULT '0',
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  PRIMARY KEY (`user_id`)
);

CREATE TABLE `goals` (
  `goal_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `goal_title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action` varchar(999) NOT NULL,
  `deadline` date NOT NULL,
  `status` int NOT NULL,
  `evaluation` varchar(10) DEFAULT NULL,
  `evaluationed_at` date DEFAULT NULL,
  `del_flg` int NOT NULL DEFAULT '0',
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  PRIMARY KEY (`goal_id`)
);

CREATE TABLE `goal_links` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `goal_id_01` int NOT NULL,
  `goal_id_02` int NOT NULL,
  `del_flg` int NOT NULL DEFAULT '0',
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  PRIMARY KEY (`id`)
);