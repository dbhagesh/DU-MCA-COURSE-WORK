--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `authentication`
--

CREATE TABLE `authentication` (
  `login_id` int(11) NOT NULL,
  `password` varchar(60) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `ISBN` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `author` varchar(60) NOT NULL,
  `available` varchar(60) NOT NULL,
  `title` varchar(60) NOT NULL,
  `issue_date` date NOT NULL,
  `due_date` date NOT NULL,
  `date` varchar(60) NOT NULL,
  `mem_id` int(11) NOT NULL,
  `pub_id` int(11) NOT NULL,
  `slot` int(20) NOT NULL,
  `floor` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE `librarian` (
  `lib_id` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `DOB` date NOT NULL,
  `first` varchar(60) NOT NULL,
  `last` varchar(60) NOT NULL,
  `login_id` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `slot` int(20) NOT NULL,
  `floor` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `p_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `amount` int(11) NOT NULL,
  `mem_id` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `phone`
--

CREATE TABLE `phone` (
  `lib_id` int(11) NOT NULL,
  `phone` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `phone_no`
--

CREATE TABLE `phone_no` (
  `mem_id` int(11) NOT NULL,
  `phone_no` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `pub_id` int(11) NOT NULL,
  `name` varchar(60) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `reading room`
--

CREATE TABLE `reading room` (
  `room` int(11) NOT NULL,
  `tableno` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `first` varchar(60) NOT NULL,
  `last` varchar(60) NOT NULL,
  `exp_date` date NOT NULL,
  `address` varchar(60) NOT NULL,
  `DOB` date NOT NULL,
  `mem_id` int(11) NOT NULL,
  `room` int(11) NOT NULL,
  `tableno` int(11) NOT NULL
) 

-- --------------------------------------------------------

--
-- Table structure for table `update`
--

CREATE TABLE `update` (
  `ISBN` int(11) NOT NULL,
  `lib_id` int(11) NOT NULL,
  `date` date NOT NULL
) 

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authentication`
--
ALTER TABLE `authentication`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`ISBN`),
  ADD KEY `book1` (`mem_id`),
  ADD KEY `book2` (`pub_id`),
  ADD KEY `book76` (`slot`);

--
-- Indexes for table `librarian`
--
ALTER TABLE `librarian`
  ADD PRIMARY KEY (`lib_id`),
  ADD KEY `lib1` (`login_id`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`slot`,`floor`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`p_id`),
  ADD KEY `payment1` (`mem_id`);

--
-- Indexes for table `phone`
--
ALTER TABLE `phone`
  ADD PRIMARY KEY (`lib_id`,`phone`);

--
-- Indexes for table `phone_no`
--
ALTER TABLE `phone_no`
  ADD PRIMARY KEY (`mem_id`,`phone_no`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`pub_id`);

--
-- Indexes for table `reading room`
--
ALTER TABLE `reading room`
  ADD PRIMARY KEY (`room`,`tableno`) USING BTREE;

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`mem_id`),
  ADD KEY `student1` (`room`);

--
-- Indexes for table `update`
--
ALTER TABLE `update`
  ADD PRIMARY KEY (`ISBN`,`lib_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book1` FOREIGN KEY (`mem_id`) REFERENCES `student` (`mem_id`),
  ADD CONSTRAINT `book2` FOREIGN KEY (`pub_id`) REFERENCES `publisher` (`pub_id`),
  ADD CONSTRAINT `book76` FOREIGN KEY (`slot`) REFERENCES `location` (`slot`),
  ADD CONSTRAINT `book87` FOREIGN KEY (`floor`) REFERENCES `location`(`floor`);

--
-- Constraints for table `librarian`
--
ALTER TABLE `librarian`
  ADD CONSTRAINT `lib1` FOREIGN KEY (`login_id`) REFERENCES `authentication` (`login_id`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment1` FOREIGN KEY (`mem_id`) REFERENCES `student` (`mem_id`);

--
-- Constraints for table `phone`
--
ALTER TABLE `phone`
  ADD CONSTRAINT `phone1` FOREIGN KEY (`lib_id`) REFERENCES `librarian` (`lib_id`);

--
-- Constraints for table `phone_no`
--
ALTER TABLE `phone_no`
  ADD CONSTRAINT `phoneno1` FOREIGN KEY (`mem_id`) REFERENCES `student` (`mem_id`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student1` FOREIGN KEY (`room`) REFERENCES `reading room` (`room`),
  ADD CONSTRAINT `student2` FOREIGN KEY (`tableno`) REFERENCES `reading room`(`tableno`);

