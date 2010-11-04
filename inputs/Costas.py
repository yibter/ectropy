class Costas:
	def __init__(self):
		from datetime import datetime
		from objects import Asset, Skill, Manpower
		from objects.Schedule import Schedule
		from objects.Task import Task
		from objects.DateRange import DateRange
		
		self.name = 'Costas'
		
		schedule = Schedule(self.name, DateRange(datetime(2010, 1, 1), datetime(2011, 1, 1)), 2)
		
		assets = {
			1: Asset(1, 'Asset 1', datetime(2010, 1, 1))
		}
		
		skills = {
			1: Skill(1, 'Skill 1', 7, 8),
			4: Skill(4, 'Skill 4', 7, 8),
			5: Skill(5, 'Skill 5', 7, 8),
			6: Skill(6, 'Skill 6', 7, 8),
			7: Skill(7, 'Skill 7', 7, 8),
			8: Skill(8, 'Skill 8', 7, 8),
			9: Skill(9, 'Skill 9', 7, 8),
			10: Skill(10, 'Skill 10', 7, 8),
			11: Skill(11, 'Skill 11', 7, 8),
			12: Skill(12, 'Skill 12', 7, 8),
			13: Skill(13, 'Skill 13', 7, 8),
			14: Skill(14, 'Skill 14', 7, 8),
			15: Skill(15, 'Skill 15', 7, 8),
			16: Skill(16, 'Skill 16', 7, 8),
			17: Skill(17, 'Skill 17', 7, 8),
			18: Skill(18, 'Skill 18', 7, 8),
			19: Skill(19, 'Skill 19', 7, 8),
			20: Skill(20, 'Skill 20', 7, 8),
			21: Skill(21, 'Skill 21', 7, 8),
			22: Skill(22, 'Skill 22', 7, 8),
			23: Skill(23, 'Skill 23', 7, 8),
			24: Skill(24, 'Skill 24', 7, 8),
			25: Skill(25, 'Skill 25', 7, 8),
			26: Skill(26, 'Skill 26', 7, 8),
			27: Skill(27, 'Skill 27', 7, 8),
			28: Skill(28, 'Skill 28', 7, 8),
			29: Skill(29, 'Skill 29', 7, 8),
			30: Skill(30, 'Skill 30', 7, 8),
			31: Skill(31, 'Skill 31', 7, 8),
			32: Skill(32, 'Skill 32', 7, 8),
			33: Skill(33, 'Skill 33', 7, 8),
			34: Skill(34, 'Skill 34', 7, 8),
			35: Skill(35, 'Skill 35', 7, 8),
			36: Skill(36, 'Skill 36', 7, 8),
			37: Skill(37, 'Skill 37', 7, 8),
			38: Skill(38, 'Skill 38', 7, 8),
			39: Skill(39, 'Skill 39', 7, 8),
			40: Skill(40, 'Skill 40', 7, 8),
			41: Skill(41, 'Skill 41', 7, 8),
			42: Skill(42, 'Skill 42', 7, 8),
			43: Skill(43, 'Skill 43', 7, 8),
			44: Skill(44, 'Skill 44', 7, 8),
			45: Skill(45, 'Skill 45', 7, 8)
		}
		
		tasks = {
			13: Task(13, 'Task 13', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			17: Task(17, 'Task 17', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			26: Task(26, 'Task 26', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			120: Task(120, 'Task 120', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			239: Task(239, 'Task 239', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			240: Task(240, 'Task 240', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			376: Task(376, 'Task 376', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			385: Task(385, 'Task 385', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			389: Task(389, 'Task 389', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			394: Task(394, 'Task 394', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			398: Task(398, 'Task 398', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			403: Task(403, 'Task 403', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			408: Task(408, 'Task 408', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			416: Task(416, 'Task 416', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			417: Task(417, 'Task 417', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			420: Task(420, 'Task 420', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			428: Task(428, 'Task 428', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			429: Task(429, 'Task 429', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			431: Task(431, 'Task 431', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			434: Task(434, 'Task 434', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			435: Task(435, 'Task 435', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			440: Task(440, 'Task 440', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			456: Task(456, 'Task 456', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			477: Task(477, 'Task 477', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			491: Task(491, 'Task 491', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			495: Task(495, 'Task 495', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			499: Task(499, 'Task 499', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			503: Task(503, 'Task 503', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			507: Task(507, 'Task 507', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			511: Task(511, 'Task 511', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			516: Task(516, 'Task 516', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			520: Task(520, 'Task 520', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			524: Task(524, 'Task 524', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			526: Task(526, 'Task 526', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			530: Task(530, 'Task 530', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			535: Task(535, 'Task 535', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			539: Task(539, 'Task 539', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			543: Task(543, 'Task 543', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			547: Task(547, 'Task 547', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			551: Task(551, 'Task 551', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			556: Task(556, 'Task 556', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			567: Task(567, 'Task 567', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			571: Task(571, 'Task 571', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			580: Task(580, 'Task 580', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			584: Task(584, 'Task 584', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			587: Task(587, 'Task 587', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			605: Task(605, 'Task 605', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			609: Task(609, 'Task 609', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			611: Task(611, 'Task 611', 7, 448, 448, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			612: Task(612, 'Task 612', 7, 448, 448, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			614: Task(614, 'Task 614', 7, 448, 448, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			615: Task(615, 'Task 615', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			616: Task(616, 'Task 616', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			617: Task(617, 'Task 617', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			618: Task(618, 'Task 618', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			620: Task(620, 'Task 620', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			621: Task(621, 'Task 621', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			622: Task(622, 'Task 622', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			624: Task(624, 'Task 624', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			625: Task(625, 'Task 625', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			626: Task(626, 'Task 626', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			628: Task(628, 'Task 628', 7, 364, 364, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			629: Task(629, 'Task 629', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			630: Task(630, 'Task 630', 7, 728, 728, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			637: Task(637, 'Task 637', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			639: Task(639, 'Task 639', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			640: Task(640, 'Task 640', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			646: Task(646, 'Task 646', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			647: Task(647, 'Task 647', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			648: Task(648, 'Task 648', 7, 1100, 1100, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			654: Task(654, 'Task 654', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			660: Task(660, 'Task 660', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			661: Task(661, 'Task 661', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			665: Task(665, 'Task 665', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			666: Task(666, 'Task 666', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			667: Task(667, 'Task 667', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			669: Task(669, 'Task 669', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			670: Task(670, 'Task 670', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			671: Task(671, 'Task 671', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			672: Task(672, 'Task 672', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			673: Task(673, 'Task 673', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			674: Task(674, 'Task 674', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			677: Task(677, 'Task 677', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			678: Task(678, 'Task 678', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			679: Task(679, 'Task 679', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			680: Task(680, 'Task 680', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			681: Task(681, 'Task 681', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			683: Task(683, 'Task 683', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			686: Task(686, 'Task 686', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			688: Task(688, 'Task 688', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			689: Task(689, 'Task 689', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			691: Task(691, 'Task 691', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			692: Task(692, 'Task 692', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			693: Task(693, 'Task 693', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			694: Task(694, 'Task 694', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			695: Task(695, 'Task 695', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			703: Task(703, 'Task 703', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			704: Task(704, 'Task 704', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			709: Task(709, 'Task 709', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			710: Task(710, 'Task 710', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			711: Task(711, 'Task 711', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			713: Task(713, 'Task 713', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			714: Task(714, 'Task 714', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			718: Task(718, 'Task 718', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			719: Task(719, 'Task 719', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			720: Task(720, 'Task 720', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			722: Task(722, 'Task 722', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			724: Task(724, 'Task 724', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			725: Task(725, 'Task 725', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			727: Task(727, 'Task 727', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			728: Task(728, 'Task 728', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			729: Task(729, 'Task 729', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			730: Task(730, 'Task 730', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			731: Task(731, 'Task 731', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			734: Task(734, 'Task 734', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			738: Task(738, 'Task 738', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			740: Task(740, 'Task 740', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			741: Task(741, 'Task 741', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			742: Task(742, 'Task 742', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			744: Task(744, 'Task 744', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			745: Task(745, 'Task 745', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			746: Task(746, 'Task 746', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			747: Task(747, 'Task 747', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			748: Task(748, 'Task 748', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			749: Task(749, 'Task 749', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			750: Task(750, 'Task 750', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			751: Task(751, 'Task 751', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			752: Task(752, 'Task 752', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			753: Task(753, 'Task 753', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			754: Task(754, 'Task 754', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			755: Task(755, 'Task 755', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			756: Task(756, 'Task 756', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			757: Task(757, 'Task 757', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			759: Task(759, 'Task 759', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			762: Task(762, 'Task 762', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			763: Task(763, 'Task 763', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			764: Task(764, 'Task 764', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			765: Task(765, 'Task 765', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			766: Task(766, 'Task 766', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			767: Task(767, 'Task 767', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			769: Task(769, 'Task 769', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			772: Task(772, 'Task 772', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			773: Task(773, 'Task 773', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			774: Task(774, 'Task 774', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			775: Task(775, 'Task 775', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			776: Task(776, 'Task 776', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			777: Task(777, 'Task 777', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			778: Task(778, 'Task 778', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			780: Task(780, 'Task 780', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			781: Task(781, 'Task 781', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			782: Task(782, 'Task 782', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			787: Task(787, 'Task 787', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			788: Task(788, 'Task 788', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			789: Task(789, 'Task 789', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			790: Task(790, 'Task 790', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			791: Task(791, 'Task 791', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			798: Task(798, 'Task 798', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			805: Task(805, 'Task 805', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			808: Task(808, 'Task 808', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			809: Task(809, 'Task 809', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			811: Task(811, 'Task 811', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			812: Task(812, 'Task 812', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			813: Task(813, 'Task 813', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			814: Task(814, 'Task 814', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			815: Task(815, 'Task 815', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			817: Task(817, 'Task 817', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			818: Task(818, 'Task 818', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			819: Task(819, 'Task 819', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			820: Task(820, 'Task 820', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			823: Task(823, 'Task 823', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			824: Task(824, 'Task 824', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			825: Task(825, 'Task 825', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			826: Task(826, 'Task 826', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			828: Task(828, 'Task 828', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			829: Task(829, 'Task 829', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			830: Task(830, 'Task 830', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			831: Task(831, 'Task 831', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			832: Task(832, 'Task 832', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			836: Task(836, 'Task 836', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			840: Task(840, 'Task 840', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			846: Task(846, 'Task 846', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			847: Task(847, 'Task 847', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			848: Task(848, 'Task 848', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			849: Task(849, 'Task 849', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			850: Task(850, 'Task 850', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			851: Task(851, 'Task 851', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			853: Task(853, 'Task 853', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			854: Task(854, 'Task 854', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			855: Task(855, 'Task 855', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			856: Task(856, 'Task 856', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			857: Task(857, 'Task 857', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			859: Task(859, 'Task 859', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			860: Task(860, 'Task 860', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			861: Task(861, 'Task 861', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			862: Task(862, 'Task 862', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			863: Task(863, 'Task 863', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			864: Task(864, 'Task 864', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			866: Task(866, 'Task 866', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			871: Task(871, 'Task 871', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			873: Task(873, 'Task 873', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			881: Task(881, 'Task 881', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			884: Task(884, 'Task 884', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			886: Task(886, 'Task 886', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			887: Task(887, 'Task 887', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			888: Task(888, 'Task 888', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			889: Task(889, 'Task 889', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			890: Task(890, 'Task 890', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			891: Task(891, 'Task 891', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			892: Task(892, 'Task 892', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			893: Task(893, 'Task 893', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			894: Task(894, 'Task 894', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			895: Task(895, 'Task 895', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			896: Task(896, 'Task 896', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			897: Task(897, 'Task 897', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			898: Task(898, 'Task 898', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			899: Task(899, 'Task 899', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			900: Task(900, 'Task 900', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			901: Task(901, 'Task 901', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			902: Task(902, 'Task 902', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			903: Task(903, 'Task 903', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			904: Task(904, 'Task 904', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			905: Task(905, 'Task 905', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			906: Task(906, 'Task 906', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			907: Task(907, 'Task 907', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			908: Task(908, 'Task 908', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			909: Task(909, 'Task 909', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			910: Task(910, 'Task 910', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			911: Task(911, 'Task 911', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			912: Task(912, 'Task 912', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			913: Task(913, 'Task 913', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			914: Task(914, 'Task 914', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			915: Task(915, 'Task 915', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			916: Task(916, 'Task 916', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			918: Task(918, 'Task 918', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			919: Task(919, 'Task 919', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			920: Task(920, 'Task 920', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			921: Task(921, 'Task 921', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			923: Task(923, 'Task 923', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			924: Task(924, 'Task 924', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			925: Task(925, 'Task 925', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			926: Task(926, 'Task 926', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			928: Task(928, 'Task 928', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			929: Task(929, 'Task 929', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			930: Task(930, 'Task 930', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			931: Task(931, 'Task 931', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			932: Task(932, 'Task 932', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			935: Task(935, 'Task 935', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			938: Task(938, 'Task 938', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			940: Task(940, 'Task 940', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			941: Task(941, 'Task 941', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			942: Task(942, 'Task 942', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			943: Task(943, 'Task 943', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			944: Task(944, 'Task 944', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			945: Task(945, 'Task 945', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			946: Task(946, 'Task 946', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			947: Task(947, 'Task 947', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			948: Task(948, 'Task 948', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			950: Task(950, 'Task 950', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			951: Task(951, 'Task 951', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			952: Task(952, 'Task 952', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			953: Task(953, 'Task 953', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			954: Task(954, 'Task 954', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			955: Task(955, 'Task 955', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			958: Task(958, 'Task 958', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			959: Task(959, 'Task 959', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			960: Task(960, 'Task 960', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			961: Task(961, 'Task 961', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			963: Task(963, 'Task 963', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			965: Task(965, 'Task 965', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			966: Task(966, 'Task 966', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			967: Task(967, 'Task 967', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			968: Task(968, 'Task 968', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			969: Task(969, 'Task 969', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			970: Task(970, 'Task 970', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			971: Task(971, 'Task 971', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			972: Task(972, 'Task 972', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			973: Task(973, 'Task 973', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			974: Task(974, 'Task 974', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			975: Task(975, 'Task 975', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			977: Task(977, 'Task 977', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			978: Task(978, 'Task 978', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			979: Task(979, 'Task 979', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			980: Task(980, 'Task 980', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			981: Task(981, 'Task 981', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			983: Task(983, 'Task 983', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			984: Task(984, 'Task 984', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			985: Task(985, 'Task 985', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			986: Task(986, 'Task 986', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			987: Task(987, 'Task 987', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			988: Task(988, 'Task 988', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			989: Task(989, 'Task 989', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			992: Task(992, 'Task 992', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			994: Task(994, 'Task 994', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1006: Task(1006, 'Task 1006', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1007: Task(1007, 'Task 1007', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1008: Task(1008, 'Task 1008', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1009: Task(1009, 'Task 1009', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1010: Task(1010, 'Task 1010', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1015: Task(1015, 'Task 1015', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1016: Task(1016, 'Task 1016', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1019: Task(1019, 'Task 1019', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1020: Task(1020, 'Task 1020', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1021: Task(1021, 'Task 1021', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1022: Task(1022, 'Task 1022', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1023: Task(1023, 'Task 1023', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1024: Task(1024, 'Task 1024', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1025: Task(1025, 'Task 1025', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1026: Task(1026, 'Task 1026', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1027: Task(1027, 'Task 1027', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1028: Task(1028, 'Task 1028', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1029: Task(1029, 'Task 1029', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1030: Task(1030, 'Task 1030', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1031: Task(1031, 'Task 1031', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1035: Task(1035, 'Task 1035', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1036: Task(1036, 'Task 1036', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1037: Task(1037, 'Task 1037', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1047: Task(1047, 'Task 1047', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1049: Task(1049, 'Task 1049', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1053: Task(1053, 'Task 1053', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1058: Task(1058, 'Task 1058', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1059: Task(1059, 'Task 1059', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1061: Task(1061, 'Task 1061', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1063: Task(1063, 'Task 1063', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1064: Task(1064, 'Task 1064', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1065: Task(1065, 'Task 1065', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1066: Task(1066, 'Task 1066', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1068: Task(1068, 'Task 1068', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1069: Task(1069, 'Task 1069', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1070: Task(1070, 'Task 1070', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1071: Task(1071, 'Task 1071', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1072: Task(1072, 'Task 1072', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1073: Task(1073, 'Task 1073', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1074: Task(1074, 'Task 1074', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1075: Task(1075, 'Task 1075', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1078: Task(1078, 'Task 1078', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1079: Task(1079, 'Task 1079', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1081: Task(1081, 'Task 1081', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1082: Task(1082, 'Task 1082', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1083: Task(1083, 'Task 1083', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1086: Task(1086, 'Task 1086', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1087: Task(1087, 'Task 1087', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1088: Task(1088, 'Task 1088', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1124: Task(1124, 'Task 1124', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1125: Task(1125, 'Task 1125', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1126: Task(1126, 'Task 1126', 7, 3100, 3100, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1127: Task(1127, 'Task 1127', 7, 4027, 4027, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1128: Task(1128, 'Task 1128', 7, 100000, 100000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1129: Task(1129, 'Task 1129', 7, 17379, 17379, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1130: Task(1130, 'Task 1130', 7, 7574, 7574, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1131: Task(1131, 'Task 1131', 7, 3300, 3300, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1132: Task(1132, 'Task 1132', 7, 8958, 8958, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1134: Task(1134, 'Task 1134', 7, 6313, 6313, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1138: Task(1138, 'Task 1138', 7, 10943, 10943, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1139: Task(1139, 'Task 1139', 7, 6000, 6000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1140: Task(1140, 'Task 1140', 7, 10, 10, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1141: Task(1141, 'Task 1141', 7, 100000, 100000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1149: Task(1149, 'Task 1149', 7, 7200, 7200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1150: Task(1150, 'Task 1150', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1163: Task(1163, 'Task 1163', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1165: Task(1165, 'Task 1165', 7, 6678, 6678, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1166: Task(1166, 'Task 1166', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1167: Task(1167, 'Task 1167', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1168: Task(1168, 'Task 1168', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1169: Task(1169, 'Task 1169', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1171: Task(1171, 'Task 1171', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1172: Task(1172, 'Task 1172', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1181: Task(1181, 'Task 1181', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1183: Task(1183, 'Task 1183', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1184: Task(1184, 'Task 1184', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1185: Task(1185, 'Task 1185', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1186: Task(1186, 'Task 1186', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1187: Task(1187, 'Task 1187', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1188: Task(1188, 'Task 1188', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1192: Task(1192, 'Task 1192', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1193: Task(1193, 'Task 1193', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1194: Task(1194, 'Task 1194', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1195: Task(1195, 'Task 1195', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1199: Task(1199, 'Task 1199', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1200: Task(1200, 'Task 1200', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1201: Task(1201, 'Task 1201', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1202: Task(1202, 'Task 1202', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1212: Task(1212, 'Task 1212', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1216: Task(1216, 'Task 1216', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1222: Task(1222, 'Task 1222', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1224: Task(1224, 'Task 1224', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1225: Task(1225, 'Task 1225', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1226: Task(1226, 'Task 1226', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1227: Task(1227, 'Task 1227', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1228: Task(1228, 'Task 1228', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1230: Task(1230, 'Task 1230', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1231: Task(1231, 'Task 1231', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1232: Task(1232, 'Task 1232', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1242: Task(1242, 'Task 1242', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1254: Task(1254, 'Task 1254', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1256: Task(1256, 'Task 1256', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1257: Task(1257, 'Task 1257', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1259: Task(1259, 'Task 1259', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1260: Task(1260, 'Task 1260', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1262: Task(1262, 'Task 1262', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1264: Task(1264, 'Task 1264', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1279: Task(1279, 'Task 1279', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1280: Task(1280, 'Task 1280', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1281: Task(1281, 'Task 1281', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1284: Task(1284, 'Task 1284', 7, 548, 548, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1290: Task(1290, 'Task 1290', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1293: Task(1293, 'Task 1293', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1295: Task(1295, 'Task 1295', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1296: Task(1296, 'Task 1296', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1308: Task(1308, 'Task 1308', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1309: Task(1309, 'Task 1309', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1310: Task(1310, 'Task 1310', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1311: Task(1311, 'Task 1311', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1312: Task(1312, 'Task 1312', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1313: Task(1313, 'Task 1313', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1315: Task(1315, 'Task 1315', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1316: Task(1316, 'Task 1316', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1317: Task(1317, 'Task 1317', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1318: Task(1318, 'Task 1318', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1319: Task(1319, 'Task 1319', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1320: Task(1320, 'Task 1320', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1321: Task(1321, 'Task 1321', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1322: Task(1322, 'Task 1322', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1323: Task(1323, 'Task 1323', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1324: Task(1324, 'Task 1324', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1325: Task(1325, 'Task 1325', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1326: Task(1326, 'Task 1326', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1327: Task(1327, 'Task 1327', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1329: Task(1329, 'Task 1329', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1330: Task(1330, 'Task 1330', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1331: Task(1331, 'Task 1331', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1332: Task(1332, 'Task 1332', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1333: Task(1333, 'Task 1333', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1334: Task(1334, 'Task 1334', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1335: Task(1335, 'Task 1335', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1336: Task(1336, 'Task 1336', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1337: Task(1337, 'Task 1337', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1338: Task(1338, 'Task 1338', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1339: Task(1339, 'Task 1339', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1340: Task(1340, 'Task 1340', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1341: Task(1341, 'Task 1341', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1344: Task(1344, 'Task 1344', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1345: Task(1345, 'Task 1345', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1346: Task(1346, 'Task 1346', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1347: Task(1347, 'Task 1347', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1348: Task(1348, 'Task 1348', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1368: Task(1368, 'Task 1368', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1369: Task(1369, 'Task 1369', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1370: Task(1370, 'Task 1370', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1374: Task(1374, 'Task 1374', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1378: Task(1378, 'Task 1378', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1382: Task(1382, 'Task 1382', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1400: Task(1400, 'Task 1400', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1401: Task(1401, 'Task 1401', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1402: Task(1402, 'Task 1402', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1415: Task(1415, 'Task 1415', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1420: Task(1420, 'Task 1420', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1421: Task(1421, 'Task 1421', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1422: Task(1422, 'Task 1422', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1434: Task(1434, 'Task 1434', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1435: Task(1435, 'Task 1435', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1438: Task(1438, 'Task 1438', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1440: Task(1440, 'Task 1440', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1441: Task(1441, 'Task 1441', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1442: Task(1442, 'Task 1442', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1444: Task(1444, 'Task 1444', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1445: Task(1445, 'Task 1445', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1446: Task(1446, 'Task 1446', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1448: Task(1448, 'Task 1448', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1449: Task(1449, 'Task 1449', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1451: Task(1451, 'Task 1451', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1452: Task(1452, 'Task 1452', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1453: Task(1453, 'Task 1453', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1454: Task(1454, 'Task 1454', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1455: Task(1455, 'Task 1455', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1458: Task(1458, 'Task 1458', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1461: Task(1461, 'Task 1461', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1467: Task(1467, 'Task 1467', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1470: Task(1470, 'Task 1470', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1471: Task(1471, 'Task 1471', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1472: Task(1472, 'Task 1472', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1473: Task(1473, 'Task 1473', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1474: Task(1474, 'Task 1474', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1475: Task(1475, 'Task 1475', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1486: Task(1486, 'Task 1486', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1487: Task(1487, 'Task 1487', 7, 224, 224, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1488: Task(1488, 'Task 1488', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1493: Task(1493, 'Task 1493', 7, 7591, 7591, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1495: Task(1495, 'Task 1495', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1502: Task(1502, 'Task 1502', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1543: Task(1543, 'Task 1543', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1544: Task(1544, 'Task 1544', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1545: Task(1545, 'Task 1545', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1557: Task(1557, 'Task 1557', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1558: Task(1558, 'Task 1558', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1567: Task(1567, 'Task 1567', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1570: Task(1570, 'Task 1570', 7, 12000, 12000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1571: Task(1571, 'Task 1571', 7, 11844, 11844, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1615: Task(1615, 'Task 1615', 7, 10, 10, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1616: Task(1616, 'Task 1616', 7, 10, 10, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1617: Task(1617, 'Task 1617', 7, 8000, 8000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1635: Task(1635, 'Task 1635', 7, 14, 14, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1636: Task(1636, 'Task 1636', 7, 28, 28, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1637: Task(1637, 'Task 1637', 7, 56, 56, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1638: Task(1638, 'Task 1638', 7, 84, 84, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1641: Task(1641, 'Task 1641', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1642: Task(1642, 'Task 1642', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1643: Task(1643, 'Task 1643', 7, 100000, 100000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1644: Task(1644, 'Task 1644', 7, 21000, 21000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1646: Task(1646, 'Task 1646', 7, 6560, 6560, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1666: Task(1666, 'Task 1666', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1694: Task(1694, 'Task 1694', 7, 15400, 15400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1714: Task(1714, 'Task 1714', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			1778: Task(1778, 'Task 1778', 7, 1800, 1800, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			2053: Task(2053, 'Task 2053', 7, 7, 7, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5008: Task(5008, 'Task 5008', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5009: Task(5009, 'Task 5009', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5216: Task(5216, 'Task 5216', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5217: Task(5217, 'Task 5217', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5218: Task(5218, 'Task 5218', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5704: Task(5704, 'Task 5704', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5705: Task(5705, 'Task 5705', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5709: Task(5709, 'Task 5709', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5734: Task(5734, 'Task 5734', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5736: Task(5736, 'Task 5736', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5738: Task(5738, 'Task 5738', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5739: Task(5739, 'Task 5739', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5740: Task(5740, 'Task 5740', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5750: Task(5750, 'Task 5750', 7, 16340, 16340, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5753: Task(5753, 'Task 5753', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5755: Task(5755, 'Task 5755', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5761: Task(5761, 'Task 5761', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5765: Task(5765, 'Task 5765', 7, 13500, 13500, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5769: Task(5769, 'Task 5769', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5771: Task(5771, 'Task 5771', 7, 100000, 100000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5790: Task(5790, 'Task 5790', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5791: Task(5791, 'Task 5791', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5792: Task(5792, 'Task 5792', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5793: Task(5793, 'Task 5793', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5794: Task(5794, 'Task 5794', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5795: Task(5795, 'Task 5795', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5826: Task(5826, 'Task 5826', 7, 14181, 14181, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5827: Task(5827, 'Task 5827', 7, 8053, 8053, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5828: Task(5828, 'Task 5828', 7, 7500, 7500, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5829: Task(5829, 'Task 5829', 7, 7500, 7500, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			5850: Task(5850, 'Task 5850', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			7266: Task(7266, 'Task 7266', 7, 100, 100, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			7286: Task(7286, 'Task 7286', 7, 10000, 10000, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			13047: Task(13047, 'Task 13047', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			13050: Task(13050, 'Task 13050', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			16808: Task(16808, 'Task 16808', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			16898: Task(16898, 'Task 16898', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			16899: Task(16899, 'Task 16899', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			16988: Task(16988, 'Task 16988', 7, 6539, 6539, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			18281: Task(18281, 'Task 18281', 7, 7021, 7021, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20388: Task(20388, 'Task 20388', 7, 3600, 3600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20389: Task(20389, 'Task 20389', 7, 2400, 2400, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20390: Task(20390, 'Task 20390', 7, 3600, 3600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20391: Task(20391, 'Task 20391', 7, 3600, 3600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20393: Task(20393, 'Task 20393', 7, 55, 55, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20402: Task(20402, 'Task 20402', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20403: Task(20403, 'Task 20403', 7, 600, 600, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange),
			20404: Task(20404, 'Task 20404', 7, 1200, 1200, [], { 'pre':[], 'concurrent':[], 'post':[], 'conflict':[] }, [], schedule.dateRange)
		}
		
		for i in range(1): tasks[13].manpowers.append(Manpower(162875+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[17].manpowers.append(Manpower(163796+1000000*i, skills[23], 0.3))
		for i in range(1): tasks[26].manpowers.append(Manpower(162870+1000000*i, skills[1], 0.2))
		for i in range(2): tasks[120].manpowers.append(Manpower(163027+1000000*i, skills[1], 0.3))
		for i in range(2): tasks[239].manpowers.append(Manpower(163917+1000000*i, skills[7], 2))
		for i in range(1): tasks[240].manpowers.append(Manpower(163918+1000000*i, skills[7], 1.5))
		for i in range(1): tasks[376].manpowers.append(Manpower(163409+1000000*i, skills[5], 1))
		for i in range(1): tasks[385].manpowers.append(Manpower(162879+1000000*i, skills[7], 0.5))
		for i in range(1): tasks[389].manpowers.append(Manpower(162881+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[394].manpowers.append(Manpower(163168+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[398].manpowers.append(Manpower(163171+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[403].manpowers.append(Manpower(163169+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[408].manpowers.append(Manpower(163170+1000000*i, skills[7], 0.2))
		for i in range(2): tasks[416].manpowers.append(Manpower(163412+1000000*i, skills[5], 6))
		for i in range(1): tasks[417].manpowers.append(Manpower(163410+1000000*i, skills[5], 1.5))
		for i in range(1): tasks[420].manpowers.append(Manpower(163408+1000000*i, skills[5], 1))
		for i in range(1): tasks[428].manpowers.append(Manpower(163541+1000000*i, skills[22], 3))
		for i in range(1): tasks[429].manpowers.append(Manpower(163540+1000000*i, skills[22], 3))
		for i in range(2): tasks[431].manpowers.append(Manpower(163806+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[434].manpowers.append(Manpower(163543+1000000*i, skills[22], 0.5))
		for i in range(1): tasks[435].manpowers.append(Manpower(163553+1000000*i, skills[22], 0.5))
		for i in range(1): tasks[440].manpowers.append(Manpower(163557+1000000*i, skills[22], 1))
		for i in range(2): tasks[456].manpowers.append(Manpower(163607+1000000*i, skills[1], 20))
		for i in range(2): tasks[456].manpowers.append(Manpower(163605+1000000*i, skills[4], 20))
		for i in range(2): tasks[456].manpowers.append(Manpower(163608+1000000*i, skills[5], 20))
		for i in range(2): tasks[456].manpowers.append(Manpower(163600+1000000*i, skills[6], 20))
		for i in range(2): tasks[456].manpowers.append(Manpower(163606+1000000*i, skills[7], 20))
		for i in range(1): tasks[477].manpowers.append(Manpower(163172+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[491].manpowers.append(Manpower(163919+1000000*i, skills[7], 0.7))
		for i in range(1): tasks[495].manpowers.append(Manpower(163180+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[499].manpowers.append(Manpower(163181+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[503].manpowers.append(Manpower(163182+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[507].manpowers.append(Manpower(163174+1000000*i, skills[7], 0.22))
		for i in range(1): tasks[511].manpowers.append(Manpower(163179+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[516].manpowers.append(Manpower(163176+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[520].manpowers.append(Manpower(163177+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[524].manpowers.append(Manpower(163178+1000000*i, skills[7], 0.1))
		for i in range(4): tasks[526].manpowers.append(Manpower(163306+1000000*i, skills[6], 3))
		for i in range(2): tasks[530].manpowers.append(Manpower(163186+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[535].manpowers.append(Manpower(163187+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[539].manpowers.append(Manpower(163190+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[543].manpowers.append(Manpower(163191+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[547].manpowers.append(Manpower(163188+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[551].manpowers.append(Manpower(163189+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[556].manpowers.append(Manpower(163193+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[567].manpowers.append(Manpower(163196+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[571].manpowers.append(Manpower(163195+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[580].manpowers.append(Manpower(163194+1000000*i, skills[7], 0.1))
		for i in range(1): tasks[584].manpowers.append(Manpower(163035+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[587].manpowers.append(Manpower(163197+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[605].manpowers.append(Manpower(163702+1000000*i, skills[6], 3))
		for i in range(1): tasks[605].manpowers.append(Manpower(163701+1000000*i, skills[1], 3))
		for i in range(1): tasks[609].manpowers.append(Manpower(163700+1000000*i, skills[1], 1))
		for i in range(1): tasks[611].manpowers.append(Manpower(163795+1000000*i, skills[1], 1))
		for i in range(2): tasks[612].manpowers.append(Manpower(163704+1000000*i, skills[1], 4))
		for i in range(2): tasks[614].manpowers.append(Manpower(163706+1000000*i, skills[1], 2))
		for i in range(2): tasks[615].manpowers.append(Manpower(163534+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[616].manpowers.append(Manpower(163707+1000000*i, skills[23], 1))
		for i in range(2): tasks[617].manpowers.append(Manpower(163793+1000000*i, skills[23], 1))
		for i in range(1): tasks[618].manpowers.append(Manpower(163794+1000000*i, skills[23], 1))
		for i in range(1): tasks[620].manpowers.append(Manpower(163711+1000000*i, skills[1], 2))
		for i in range(1): tasks[621].manpowers.append(Manpower(163532+1000000*i, skills[6], 0.6))
		for i in range(1): tasks[622].manpowers.append(Manpower(163712+1000000*i, skills[4], 2))
		for i in range(2): tasks[624].manpowers.append(Manpower(163560+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[625].manpowers.append(Manpower(163713+1000000*i, skills[4], 0.5))
		for i in range(2): tasks[626].manpowers.append(Manpower(163715+1000000*i, skills[23], 0.7))
		for i in range(1): tasks[628].manpowers.append(Manpower(163692+1000000*i, skills[4], 1))
		for i in range(2): tasks[629].manpowers.append(Manpower(163694+1000000*i, skills[6], 2))
		for i in range(1): tasks[630].manpowers.append(Manpower(163716+1000000*i, skills[4], 1))
		for i in range(1): tasks[637].manpowers.append(Manpower(163568+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[639].manpowers.append(Manpower(163164+1000000*i, skills[22], 0.1))
		for i in range(2): tasks[639].manpowers.append(Manpower(163163+1000000*i, skills[7], 1))
		for i in range(2): tasks[640].manpowers.append(Manpower(163161+1000000*i, skills[7], 0.5))
		for i in range(1): tasks[640].manpowers.append(Manpower(163160+1000000*i, skills[22], 0.1))
		for i in range(2): tasks[646].manpowers.append(Manpower(163718+1000000*i, skills[6], 1.5))
		for i in range(3): tasks[647].manpowers.append(Manpower(163721+1000000*i, skills[6], 1.5))
		for i in range(1): tasks[648].manpowers.append(Manpower(163722+1000000*i, skills[7], 8))
		for i in range(2): tasks[654].manpowers.append(Manpower(163802+1000000*i, skills[7], 4))
		for i in range(1): tasks[660].manpowers.append(Manpower(163201+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[661].manpowers.append(Manpower(163740+1000000*i, skills[7], 0.2))
		for i in range(2): tasks[665].manpowers.append(Manpower(163738+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[666].manpowers.append(Manpower(163640+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[667].manpowers.append(Manpower(163200+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[669].manpowers.append(Manpower(163642+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[670].manpowers.append(Manpower(163202+1000000*i, skills[7], 2))
		for i in range(2): tasks[671].manpowers.append(Manpower(163646+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[672].manpowers.append(Manpower(163644+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[673].manpowers.append(Manpower(163658+1000000*i, skills[6], 0.6))
		for i in range(4): tasks[674].manpowers.append(Manpower(163652+1000000*i, skills[6], 1))
		for i in range(2): tasks[677].manpowers.append(Manpower(163166+1000000*i, skills[7], 2.5))
		for i in range(2): tasks[678].manpowers.append(Manpower(163627+1000000*i, skills[6], 0.8))
		for i in range(1): tasks[679].manpowers.append(Manpower(162950+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[680].manpowers.append(Manpower(162949+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[681].manpowers.append(Manpower(163653+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[683].manpowers.append(Manpower(163391+1000000*i, skills[4], 4))
		for i in range(2): tasks[686].manpowers.append(Manpower(163666+1000000*i, skills[6], 1))
		for i in range(1): tasks[688].manpowers.append(Manpower(162856+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[689].manpowers.append(Manpower(163741+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[691].manpowers.append(Manpower(163156+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[692].manpowers.append(Manpower(163158+1000000*i, skills[4], 0.4))
		for i in range(1): tasks[693].manpowers.append(Manpower(163667+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[694].manpowers.append(Manpower(163668+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[695].manpowers.append(Manpower(163670+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[703].manpowers.append(Manpower(162864+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[704].manpowers.append(Manpower(162865+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[709].manpowers.append(Manpower(163671+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[710].manpowers.append(Manpower(163674+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[711].manpowers.append(Manpower(163673+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[713].manpowers.append(Manpower(162901+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[714].manpowers.append(Manpower(163678+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[718].manpowers.append(Manpower(163680+1000000*i, skills[1], 0.4))
		for i in range(1): tasks[719].manpowers.append(Manpower(163676+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[720].manpowers.append(Manpower(163675+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[722].manpowers.append(Manpower(163677+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[724].manpowers.append(Manpower(163214+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[725].manpowers.append(Manpower(163395+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[727].manpowers.append(Manpower(163396+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[728].manpowers.append(Manpower(163397+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[729].manpowers.append(Manpower(163404+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[730].manpowers.append(Manpower(163402+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[731].manpowers.append(Manpower(163403+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[734].manpowers.append(Manpower(163421+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[738].manpowers.append(Manpower(163422+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[740].manpowers.append(Manpower(163429+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[741].manpowers.append(Manpower(163432+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[742].manpowers.append(Manpower(163431+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[744].manpowers.append(Manpower(163433+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[745].manpowers.append(Manpower(163434+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[746].manpowers.append(Manpower(163435+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[747].manpowers.append(Manpower(163437+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[748].manpowers.append(Manpower(163438+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[749].manpowers.append(Manpower(163436+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[750].manpowers.append(Manpower(163312+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[751].manpowers.append(Manpower(163450+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[752].manpowers.append(Manpower(163451+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[753].manpowers.append(Manpower(163453+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[754].manpowers.append(Manpower(162877+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[755].manpowers.append(Manpower(162885+1000000*i, skills[6], 0.1))
		for i in range(2): tasks[756].manpowers.append(Manpower(162882+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[757].manpowers.append(Manpower(163452+1000000*i, skills[5], 0.1))
		for i in range(2): tasks[759].manpowers.append(Manpower(162883+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[762].manpowers.append(Manpower(162837+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[763].manpowers.append(Manpower(163457+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[764].manpowers.append(Manpower(162838+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[765].manpowers.append(Manpower(163459+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[766].manpowers.append(Manpower(163473+1000000*i, skills[5], 0.4))
		for i in range(1): tasks[767].manpowers.append(Manpower(162839+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[769].manpowers.append(Manpower(162902+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[772].manpowers.append(Manpower(163477+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[773].manpowers.append(Manpower(163475+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[774].manpowers.append(Manpower(163467+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[775].manpowers.append(Manpower(163466+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[776].manpowers.append(Manpower(162903+1000000*i, skills[6], 0.8))
		for i in range(1): tasks[777].manpowers.append(Manpower(163462+1000000*i, skills[5], 0.1))
		for i in range(2): tasks[778].manpowers.append(Manpower(162858+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[780].manpowers.append(Manpower(163461+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[781].manpowers.append(Manpower(163476+1000000*i, skills[5], 0.6))
		for i in range(1): tasks[782].manpowers.append(Manpower(163243+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[787].manpowers.append(Manpower(163734+1000000*i, skills[7], 1))
		for i in range(1): tasks[788].manpowers.append(Manpower(163464+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[789].manpowers.append(Manpower(163465+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[790].manpowers.append(Manpower(162867+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[791].manpowers.append(Manpower(162868+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[798].manpowers.append(Manpower(162869+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[805].manpowers.append(Manpower(162874+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[808].manpowers.append(Manpower(163011+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[809].manpowers.append(Manpower(163010+1000000*i, skills[6], 0.8))
		for i in range(1): tasks[811].manpowers.append(Manpower(163009+1000000*i, skills[6], 1))
		for i in range(1): tasks[812].manpowers.append(Manpower(162889+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[813].manpowers.append(Manpower(162887+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[814].manpowers.append(Manpower(163482+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[815].manpowers.append(Manpower(162890+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[817].manpowers.append(Manpower(163496+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[818].manpowers.append(Manpower(163481+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[819].manpowers.append(Manpower(162888+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[820].manpowers.append(Manpower(163012+1000000*i, skills[6], 1.5))
		for i in range(1): tasks[823].manpowers.append(Manpower(163478+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[824].manpowers.append(Manpower(163502+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[825].manpowers.append(Manpower(163503+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[826].manpowers.append(Manpower(163498+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[828].manpowers.append(Manpower(163500+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[829].manpowers.append(Manpower(163525+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[830].manpowers.append(Manpower(163501+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[831].manpowers.append(Manpower(163013+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[832].manpowers.append(Manpower(163014+1000000*i, skills[6], 2.8))
		for i in range(1): tasks[836].manpowers.append(Manpower(163505+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[840].manpowers.append(Manpower(163280+1000000*i, skills[7], 0.5))
		for i in range(2): tasks[846].manpowers.append(Manpower(162913+1000000*i, skills[6], 1))
		for i in range(2): tasks[847].manpowers.append(Manpower(162915+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[848].manpowers.append(Manpower(162911+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[849].manpowers.append(Manpower(162904+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[850].manpowers.append(Manpower(162923+1000000*i, skills[6], 1))
		for i in range(2): tasks[851].manpowers.append(Manpower(162919+1000000*i, skills[6], 1))
		for i in range(1): tasks[853].manpowers.append(Manpower(163504+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[854].manpowers.append(Manpower(163524+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[855].manpowers.append(Manpower(163507+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[856].manpowers.append(Manpower(163499+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[857].manpowers.append(Manpower(163509+1000000*i, skills[5], 0.2))
		for i in range(2): tasks[859].manpowers.append(Manpower(162927+1000000*i, skills[6], 1))
		for i in range(2): tasks[860].manpowers.append(Manpower(162929+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[861].manpowers.append(Manpower(163838+1000000*i, skills[6], 3.5))
		for i in range(2): tasks[862].manpowers.append(Manpower(162921+1000000*i, skills[6], 1))
		for i in range(2): tasks[863].manpowers.append(Manpower(162925+1000000*i, skills[6], 1.3))
		for i in range(1): tasks[864].manpowers.append(Manpower(163510+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[866].manpowers.append(Manpower(163538+1000000*i, skills[5], 1))
		for i in range(1): tasks[871].manpowers.append(Manpower(163512+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[873].manpowers.append(Manpower(163508+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[881].manpowers.append(Manpower(163034+1000000*i, skills[6], 0.2))
		for i in range(4): tasks[884].manpowers.append(Manpower(163380+1000000*i, skills[6], 0.4))
		for i in range(2): tasks[886].manpowers.append(Manpower(163377+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[887].manpowers.append(Manpower(163036+1000000*i, skills[6], 0.4))
		for i in range(2): tasks[888].manpowers.append(Manpower(163100+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[889].manpowers.append(Manpower(163102+1000000*i, skills[6], 1.5))
		for i in range(2): tasks[890].manpowers.append(Manpower(163375+1000000*i, skills[6], 1))
		for i in range(2): tasks[891].manpowers.append(Manpower(162853+1000000*i, skills[6], 1))
		for i in range(1): tasks[892].manpowers.append(Manpower(163483+1000000*i, skills[5], 0.2))
		for i in range(2): tasks[893].manpowers.append(Manpower(162855+1000000*i, skills[6], 1))
		for i in range(1): tasks[894].manpowers.append(Manpower(162873+1000000*i, skills[6], 1))
		for i in range(1): tasks[895].manpowers.append(Manpower(162842+1000000*i, skills[4], 0.2))
		for i in range(2): tasks[896].manpowers.append(Manpower(162931+1000000*i, skills[6], 0.4))
		for i in range(2): tasks[897].manpowers.append(Manpower(162933+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[898].manpowers.append(Manpower(162843+1000000*i, skills[4], 0.2))
		for i in range(1): tasks[899].manpowers.append(Manpower(163486+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[900].manpowers.append(Manpower(163488+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[901].manpowers.append(Manpower(162953+1000000*i, skills[4], 1.3))
		for i in range(1): tasks[902].manpowers.append(Manpower(163489+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[903].manpowers.append(Manpower(163487+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[904].manpowers.append(Manpower(163491+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[905].manpowers.append(Manpower(162954+1000000*i, skills[4], 0.5))
		for i in range(1): tasks[906].manpowers.append(Manpower(163492+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[907].manpowers.append(Manpower(163513+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[908].manpowers.append(Manpower(163103+1000000*i, skills[4], 1))
		for i in range(1): tasks[909].manpowers.append(Manpower(162861+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[910].manpowers.append(Manpower(162844+1000000*i, skills[4], 0.2))
		for i in range(1): tasks[911].manpowers.append(Manpower(162845+1000000*i, skills[1], 0.3))
		for i in range(1): tasks[912].manpowers.append(Manpower(162846+1000000*i, skills[1], 0.3))
		for i in range(1): tasks[913].manpowers.append(Manpower(162847+1000000*i, skills[1], 0.1))
		for i in range(1): tasks[914].manpowers.append(Manpower(162849+1000000*i, skills[1], 0.2))
		for i in range(1): tasks[915].manpowers.append(Manpower(162848+1000000*i, skills[1], 0.1))
		for i in range(1): tasks[916].manpowers.append(Manpower(163517+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[918].manpowers.append(Manpower(163257+1000000*i, skills[1], 0.9))
		for i in range(2): tasks[919].manpowers.append(Manpower(162952+1000000*i, skills[4], 1.5))
		for i in range(1): tasks[920].manpowers.append(Manpower(163518+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[921].manpowers.append(Manpower(162900+1000000*i, skills[4], 3))
		for i in range(1): tasks[923].manpowers.append(Manpower(162871+1000000*i, skills[1], 0.5))
		for i in range(1): tasks[924].manpowers.append(Manpower(162863+1000000*i, skills[4], 1.5))
		for i in range(1): tasks[925].manpowers.append(Manpower(162862+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[926].manpowers.append(Manpower(162957+1000000*i, skills[4], 0.8))
		for i in range(2): tasks[928].manpowers.append(Manpower(162959+1000000*i, skills[1], 0.4))
		for i in range(1): tasks[929].manpowers.append(Manpower(162969+1000000*i, skills[1], 1))
		for i in range(1): tasks[930].manpowers.append(Manpower(162962+1000000*i, skills[1], 2.5))
		for i in range(3): tasks[931].manpowers.append(Manpower(162968+1000000*i, skills[1], 1))
		for i in range(3): tasks[932].manpowers.append(Manpower(162967+1000000*i, skills[1], 0.5))
		for i in range(3): tasks[935].manpowers.append(Manpower(163026+1000000*i, skills[1], 0.2))
		for i in range(2): tasks[938].manpowers.append(Manpower(163029+1000000*i, skills[1], 0.1))
		for i in range(1): tasks[940].manpowers.append(Manpower(162979+1000000*i, skills[1], 0.2))
		for i in range(1): tasks[941].manpowers.append(Manpower(162980+1000000*i, skills[1], 0.25))
		for i in range(2): tasks[942].manpowers.append(Manpower(163062+1000000*i, skills[1], 0.2))
		for i in range(2): tasks[943].manpowers.append(Manpower(163063+1000000*i, skills[1], 3))
		for i in range(2): tasks[944].manpowers.append(Manpower(163031+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[945].manpowers.append(Manpower(163033+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[946].manpowers.append(Manpower(163038+1000000*i, skills[1], 0.3))
		for i in range(2): tasks[947].manpowers.append(Manpower(163040+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[948].manpowers.append(Manpower(163042+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[950].manpowers.append(Manpower(163044+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[951].manpowers.append(Manpower(163048+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[952].manpowers.append(Manpower(162896+1000000*i, skills[5], 4))
		for i in range(2): tasks[953].manpowers.append(Manpower(163046+1000000*i, skills[1], 0.2))
		for i in range(2): tasks[954].manpowers.append(Manpower(163050+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[955].manpowers.append(Manpower(163052+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[958].manpowers.append(Manpower(163381+1000000*i, skills[5], 1))
		for i in range(2): tasks[959].manpowers.append(Manpower(163054+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[960].manpowers.append(Manpower(163056+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[961].manpowers.append(Manpower(163058+1000000*i, skills[1], 0.2))
		for i in range(1): tasks[963].manpowers.append(Manpower(163516+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[965].manpowers.append(Manpower(163519+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[966].manpowers.append(Manpower(163521+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[967].manpowers.append(Manpower(163515+1000000*i, skills[5], 0.2))
		for i in range(2): tasks[968].manpowers.append(Manpower(163060+1000000*i, skills[1], 0.2))
		for i in range(1): tasks[969].manpowers.append(Manpower(162987+1000000*i, skills[5], 4))
		for i in range(1): tasks[970].manpowers.append(Manpower(162988+1000000*i, skills[5], 3))
		for i in range(2): tasks[971].manpowers.append(Manpower(163075+1000000*i, skills[5], 2))
		for i in range(2): tasks[972].manpowers.append(Manpower(162841+1000000*i, skills[5], 1.3))
		for i in range(2): tasks[973].manpowers.append(Manpower(163073+1000000*i, skills[5], 0.9))
		for i in range(2): tasks[974].manpowers.append(Manpower(163071+1000000*i, skills[5], 0.2))
		for i in range(2): tasks[975].manpowers.append(Manpower(163077+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[977].manpowers.append(Manpower(163079+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[978].manpowers.append(Manpower(163081+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[979].manpowers.append(Manpower(163083+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[980].manpowers.append(Manpower(163085+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[981].manpowers.append(Manpower(163087+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[983].manpowers.append(Manpower(163091+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[984].manpowers.append(Manpower(163093+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[985].manpowers.append(Manpower(163095+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[986].manpowers.append(Manpower(163097+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[987].manpowers.append(Manpower(163490+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[988].manpowers.append(Manpower(162859+1000000*i, skills[22], 0.5))
		for i in range(1): tasks[989].manpowers.append(Manpower(162860+1000000*i, skills[22], 0.2))
		for i in range(1): tasks[992].manpowers.append(Manpower(163528+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[994].manpowers.append(Manpower(163523+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[1006].manpowers.append(Manpower(163535+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[1007].manpowers.append(Manpower(163537+1000000*i, skills[5], 1))
		for i in range(1): tasks[1008].manpowers.append(Manpower(163407+1000000*i, skills[4], 1))
		for i in range(1): tasks[1009].manpowers.append(Manpower(163830+1000000*i, skills[1], 0.4))
		for i in range(9): tasks[1010].manpowers.append(Manpower(163552+1000000*i, skills[6], 9))
		for i in range(1): tasks[1015].manpowers.append(Manpower(163203+1000000*i, skills[6], 0.6))
		for i in range(1): tasks[1016].manpowers.append(Manpower(163204+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[1019].manpowers.append(Manpower(163209+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[1020].manpowers.append(Manpower(163210+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1021].manpowers.append(Manpower(163157+1000000*i, skills[4], 0.4))
		for i in range(1): tasks[1022].manpowers.append(Manpower(163250+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[1023].manpowers.append(Manpower(163249+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1024].manpowers.append(Manpower(163247+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[1025].manpowers.append(Manpower(163245+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1026].manpowers.append(Manpower(163211+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[1027].manpowers.append(Manpower(163248+1000000*i, skills[6], 0.1))
		for i in range(2): tasks[1028].manpowers.append(Manpower(163316+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[1029].manpowers.append(Manpower(163315+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[1030].manpowers.append(Manpower(163314+1000000*i, skills[6], 0.3))
		for i in range(1): tasks[1031].manpowers.append(Manpower(163251+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1035].manpowers.append(Manpower(163285+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1036].manpowers.append(Manpower(163256+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[1037].manpowers.append(Manpower(163293+1000000*i, skills[6], 5))
		for i in range(2): tasks[1047].manpowers.append(Manpower(163117+1000000*i, skills[6], 1))
		for i in range(1): tasks[1049].manpowers.append(Manpower(163116+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[1053].manpowers.append(Manpower(163127+1000000*i, skills[6], 6.3))
		for i in range(2): tasks[1058].manpowers.append(Manpower(163134+1000000*i, skills[6], 1))
		for i in range(2): tasks[1059].manpowers.append(Manpower(163136+1000000*i, skills[6], 1))
		for i in range(2): tasks[1061].manpowers.append(Manpower(163268+1000000*i, skills[5], 0.5))
		for i in range(2): tasks[1063].manpowers.append(Manpower(163270+1000000*i, skills[5], 1))
		for i in range(1): tasks[1064].manpowers.append(Manpower(163137+1000000*i, skills[4], 0.4))
		for i in range(1): tasks[1065].manpowers.append(Manpower(163138+1000000*i, skills[4], 0.2))
		for i in range(1): tasks[1066].manpowers.append(Manpower(163219+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1068].manpowers.append(Manpower(163222+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1069].manpowers.append(Manpower(163213+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1070].manpowers.append(Manpower(163221+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1071].manpowers.append(Manpower(163217+1000000*i, skills[4], 0.1))
		for i in range(2): tasks[1072].manpowers.append(Manpower(163216+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[1073].manpowers.append(Manpower(163142+1000000*i, skills[4], 0.5))
		for i in range(1): tasks[1074].manpowers.append(Manpower(163271+1000000*i, skills[5], 1))
		for i in range(1): tasks[1075].manpowers.append(Manpower(163155+1000000*i, skills[4], 0.4))
		for i in range(1): tasks[1078].manpowers.append(Manpower(163272+1000000*i, skills[5], 20))
		for i in range(3): tasks[1079].manpowers.append(Manpower(163275+1000000*i, skills[5], 12))
		for i in range(1): tasks[1081].manpowers.append(Manpower(163152+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[1082].manpowers.append(Manpower(163154+1000000*i, skills[4], 0.3))
		for i in range(1): tasks[1083].manpowers.append(Manpower(163153+1000000*i, skills[4], 0.2))
		for i in range(2): tasks[1086].manpowers.append(Manpower(163236+1000000*i, skills[5], 3.5))
		for i in range(2): tasks[1087].manpowers.append(Manpower(163235+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[1088].manpowers.append(Manpower(163260+1000000*i, skills[6], 1))
		for i in range(2): tasks[1088].manpowers.append(Manpower(163259+1000000*i, skills[5], 6))
		for i in range(1): tasks[1124].manpowers.append(Manpower(163430+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1125].manpowers.append(Manpower(163463+1000000*i, skills[6], 0.1))
		for i in range(1): tasks[1126].manpowers.append(Manpower(163359+1000000*i, skills[8], 10))
		for i in range(1): tasks[1126].manpowers.append(Manpower(163358+1000000*i, skills[10], 4))
		for i in range(1): tasks[1127].manpowers.append(Manpower(163361+1000000*i, skills[8], 15))
		for i in range(1): tasks[1127].manpowers.append(Manpower(163360+1000000*i, skills[10], 4))
		for i in range(2): tasks[1128].manpowers.append(Manpower(164193+1000000*i, skills[8], 15))
		for i in range(1): tasks[1129].manpowers.append(Manpower(163362+1000000*i, skills[10], 4))
		for i in range(1): tasks[1129].manpowers.append(Manpower(163363+1000000*i, skills[8], 10))
		for i in range(2): tasks[1130].manpowers.append(Manpower(164197+1000000*i, skills[8], 15))
		for i in range(1): tasks[1131].manpowers.append(Manpower(163364+1000000*i, skills[1], 10))
		for i in range(1): tasks[1131].manpowers.append(Manpower(163319+1000000*i, skills[10], 4))
		for i in range(2): tasks[1132].manpowers.append(Manpower(164201+1000000*i, skills[8], 15))
		for i in range(1): tasks[1134].manpowers.append(Manpower(163366+1000000*i, skills[8], 10))
		for i in range(1): tasks[1134].manpowers.append(Manpower(163365+1000000*i, skills[10], 4))
		for i in range(1): tasks[1138].manpowers.append(Manpower(163321+1000000*i, skills[10], 1))
		for i in range(1): tasks[1138].manpowers.append(Manpower(163986+1000000*i, skills[8], 12))
		for i in range(1): tasks[1139].manpowers.append(Manpower(163323+1000000*i, skills[8], 6))
		for i in range(1): tasks[1139].manpowers.append(Manpower(163322+1000000*i, skills[10], 10))
		for i in range(1): tasks[1140].manpowers.append(Manpower(163324+1000000*i, skills[8], 20))
		for i in range(1): tasks[1140].manpowers.append(Manpower(163371+1000000*i, skills[11], 4))
		for i in range(1): tasks[1141].manpowers.append(Manpower(163326+1000000*i, skills[8], 4.3))
		for i in range(1): tasks[1141].manpowers.append(Manpower(163325+1000000*i, skills[10], 29.3))
		for i in range(1): tasks[1149].manpowers.append(Manpower(163833+1000000*i, skills[8], 6))
		for i in range(1): tasks[1149].manpowers.append(Manpower(163351+1000000*i, skills[10], 60))
		for i in range(1): tasks[1150].manpowers.append(Manpower(163458+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[1163].manpowers.append(Manpower(163809+1000000*i, skills[22], 1))
		for i in range(2): tasks[1165].manpowers.append(Manpower(164091+1000000*i, skills[8], 100))
		for i in range(1): tasks[1166].manpowers.append(Manpower(163372+1000000*i, skills[8], 25))
		for i in range(1): tasks[1166].manpowers.append(Manpower(163348+1000000*i, skills[10], 25))
		for i in range(1): tasks[1167].manpowers.append(Manpower(163212+1000000*i, skills[4], 0.2))
		for i in range(1): tasks[1168].manpowers.append(Manpower(163479+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1169].manpowers.append(Manpower(163506+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1171].manpowers.append(Manpower(163480+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1172].manpowers.append(Manpower(163827+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[1181].manpowers.append(Manpower(163990+1000000*i, skills[8], 8))
		for i in range(1): tasks[1183].manpowers.append(Manpower(163998+1000000*i, skills[8], 30))
		for i in range(1): tasks[1184].manpowers.append(Manpower(164016+1000000*i, skills[8], 40))
		for i in range(2): tasks[1185].manpowers.append(Manpower(164147+1000000*i, skills[8], 8))
		for i in range(2): tasks[1186].manpowers.append(Manpower(164006+1000000*i, skills[8], 40))
		for i in range(1): tasks[1187].manpowers.append(Manpower(164009+1000000*i, skills[8], 20))
		for i in range(1): tasks[1188].manpowers.append(Manpower(163615+1000000*i, skills[22], 2))
		for i in range(1): tasks[1188].manpowers.append(Manpower(163612+1000000*i, skills[1], 2))
		for i in range(2): tasks[1188].manpowers.append(Manpower(163611+1000000*i, skills[4], 2))
		for i in range(2): tasks[1188].manpowers.append(Manpower(163614+1000000*i, skills[5], 2))
		for i in range(1): tasks[1188].manpowers.append(Manpower(163609+1000000*i, skills[6], 2))
		for i in range(1): tasks[1188].manpowers.append(Manpower(163616+1000000*i, skills[7], 2))
		for i in range(1): tasks[1192].manpowers.append(Manpower(163454+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1193].manpowers.append(Manpower(163455+1000000*i, skills[5], 0.1))
		for i in range(2): tasks[1194].manpowers.append(Manpower(162851+1000000*i, skills[7], 1))
		for i in range(1): tasks[1195].manpowers.append(Manpower(162886+1000000*i, skills[6], 0.4))
		for i in range(2): tasks[1199].manpowers.append(Manpower(162985+1000000*i, skills[5], 4))
		for i in range(1): tasks[1200].manpowers.append(Manpower(162989+1000000*i, skills[5], 1.5))
		for i in range(2): tasks[1201].manpowers.append(Manpower(163238+1000000*i, skills[5], 2))
		for i in range(2): tasks[1202].manpowers.append(Manpower(163242+1000000*i, skills[5], 3))
		for i in range(2): tasks[1212].manpowers.append(Manpower(163320+1000000*i, skills[7], 1))
		for i in range(2): tasks[1216].manpowers.append(Manpower(163007+1000000*i, skills[7], 1))
		for i in range(2): tasks[1222].manpowers.append(Manpower(163125+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[1224].manpowers.append(Manpower(163141+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1225].manpowers.append(Manpower(163198+1000000*i, skills[6], 1.4))
		for i in range(1): tasks[1226].manpowers.append(Manpower(163218+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1227].manpowers.append(Manpower(163220+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1228].manpowers.append(Manpower(163224+1000000*i, skills[4], 0.1))
		for i in range(3): tasks[1230].manpowers.append(Manpower(163022+1000000*i, skills[1], 0.1))
		for i in range(3): tasks[1231].manpowers.append(Manpower(163019+1000000*i, skills[1], 0.1))
		for i in range(2): tasks[1232].manpowers.append(Manpower(163069+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[1242].manpowers.append(Manpower(163390+1000000*i, skills[7], 1.5))
		for i in range(1): tasks[1254].manpowers.append(Manpower(163469+1000000*i, skills[5], 0.3))
		for i in range(1): tasks[1256].manpowers.append(Manpower(163497+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1257].manpowers.append(Manpower(163494+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1259].manpowers.append(Manpower(163493+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1260].manpowers.append(Manpower(163495+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1262].manpowers.append(Manpower(163485+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1264].manpowers.append(Manpower(163484+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1279].manpowers.append(Manpower(163527+1000000*i, skills[1], 0.1))
		for i in range(1): tasks[1280].manpowers.append(Manpower(163529+1000000*i, skills[4], 0.2))
		for i in range(1): tasks[1281].manpowers.append(Manpower(163539+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1284].manpowers.append(Manpower(163695+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[1290].manpowers.append(Manpower(163598+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1293].manpowers.append(Manpower(163572+1000000*i, skills[6], 1))
		for i in range(1): tasks[1295].manpowers.append(Manpower(163556+1000000*i, skills[22], 1))
		for i in range(1): tasks[1296].manpowers.append(Manpower(163822+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1308].manpowers.append(Manpower(163400+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1309].manpowers.append(Manpower(163401+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1310].manpowers.append(Manpower(163399+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1311].manpowers.append(Manpower(163394+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1312].manpowers.append(Manpower(163398+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1313].manpowers.append(Manpower(163831+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1315].manpowers.append(Manpower(163416+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1316].manpowers.append(Manpower(163413+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1317].manpowers.append(Manpower(163420+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1318].manpowers.append(Manpower(163418+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1319].manpowers.append(Manpower(163419+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1320].manpowers.append(Manpower(163427+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1321].manpowers.append(Manpower(163415+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1322].manpowers.append(Manpower(163417+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1323].manpowers.append(Manpower(163426+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1324].manpowers.append(Manpower(163414+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1325].manpowers.append(Manpower(163423+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1326].manpowers.append(Manpower(163424+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1327].manpowers.append(Manpower(163425+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1329].manpowers.append(Manpower(163428+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1330].manpowers.append(Manpower(163456+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1331].manpowers.append(Manpower(163439+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1332].manpowers.append(Manpower(163448+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1333].manpowers.append(Manpower(163442+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1334].manpowers.append(Manpower(163440+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1335].manpowers.append(Manpower(163444+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1336].manpowers.append(Manpower(163445+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1337].manpowers.append(Manpower(163443+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1338].manpowers.append(Manpower(163449+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1339].manpowers.append(Manpower(163446+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1340].manpowers.append(Manpower(163447+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1341].manpowers.append(Manpower(163441+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1344].manpowers.append(Manpower(163367+1000000*i, skills[8], 4))
		for i in range(2): tasks[1345].manpowers.append(Manpower(164244+1000000*i, skills[6], 4))
		for i in range(1): tasks[1346].manpowers.append(Manpower(163368+1000000*i, skills[8], 4))
		for i in range(1): tasks[1347].manpowers.append(Manpower(163369+1000000*i, skills[8], 4))
		for i in range(1): tasks[1348].manpowers.append(Manpower(163370+1000000*i, skills[8], 4))
		for i in range(2): tasks[1368].manpowers.append(Manpower(163736+1000000*i, skills[5], 0.5))
		for i in range(1): tasks[1369].manpowers.append(Manpower(162905+1000000*i, skills[6], 5))
		for i in range(1): tasks[1369].manpowers.append(Manpower(163016+1000000*i, skills[23], 0.4))
		for i in range(1): tasks[1370].manpowers.append(Manpower(163255+1000000*i, skills[6], 5))
		for i in range(1): tasks[1370].manpowers.append(Manpower(163382+1000000*i, skills[23], 0.3))
		for i in range(2): tasks[1374].manpowers.append(Manpower(163384+1000000*i, skills[7], 1))
		for i in range(1): tasks[1378].manpowers.append(Manpower(163386+1000000*i, skills[7], 0.3))
		for i in range(1): tasks[1382].manpowers.append(Manpower(163385+1000000*i, skills[7], 0.3))
		for i in range(2): tasks[1400].manpowers.append(Manpower(163393+1000000*i, skills[4], 4))
		for i in range(1): tasks[1401].manpowers.append(Manpower(163406+1000000*i, skills[4], 1))
		for i in range(1): tasks[1402].manpowers.append(Manpower(163471+1000000*i, skills[5], 0.4))
		for i in range(1): tasks[1415].manpowers.append(Manpower(163520+1000000*i, skills[5], 0.1))
		for i in range(2): tasks[1420].manpowers.append(Manpower(163388+1000000*i, skills[7], 1))
		for i in range(2): tasks[1421].manpowers.append(Manpower(163561+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[1422].manpowers.append(Manpower(163625+1000000*i, skills[6], 1))
		for i in range(1): tasks[1434].manpowers.append(Manpower(163622+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[1435].manpowers.append(Manpower(163672+1000000*i, skills[6], 0.4))
		for i in range(1): tasks[1438].manpowers.append(Manpower(163679+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[1440].manpowers.append(Manpower(163832+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1441].manpowers.append(Manpower(163468+1000000*i, skills[5], 1))
		for i in range(1): tasks[1442].manpowers.append(Manpower(163472+1000000*i, skills[5], 0.4))
		for i in range(1): tasks[1444].manpowers.append(Manpower(163474+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1445].manpowers.append(Manpower(163514+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1446].manpowers.append(Manpower(163522+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[1448].manpowers.append(Manpower(163530+1000000*i, skills[4], 0.1))
		for i in range(1): tasks[1449].manpowers.append(Manpower(163536+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[1451].manpowers.append(Manpower(163542+1000000*i, skills[22], 1))
		for i in range(1): tasks[1452].manpowers.append(Manpower(163554+1000000*i, skills[22], 0.5))
		for i in range(2): tasks[1453].manpowers.append(Manpower(163927+1000000*i, skills[22], 1))
		for i in range(1): tasks[1454].manpowers.append(Manpower(163562+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1455].manpowers.append(Manpower(163563+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[1458].manpowers.append(Manpower(163565+1000000*i, skills[6], 0.1))
		for i in range(4): tasks[1461].manpowers.append(Manpower(163620+1000000*i, skills[6], 3))
		for i in range(1): tasks[1467].manpowers.append(Manpower(163623+1000000*i, skills[6], 0.8))
		for i in range(2): tasks[1470].manpowers.append(Manpower(163648+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[1471].manpowers.append(Manpower(163655+1000000*i, skills[6], 1))
		for i in range(2): tasks[1472].manpowers.append(Manpower(163664+1000000*i, skills[6], 0.6))
		for i in range(4): tasks[1473].manpowers.append(Manpower(163684+1000000*i, skills[6], 0.6))
		for i in range(5): tasks[1474].manpowers.append(Manpower(163689+1000000*i, skills[6], 3))
		for i in range(2): tasks[1475].manpowers.append(Manpower(163691+1000000*i, skills[22], 1))
		for i in range(1): tasks[1486].manpowers.append(Manpower(163699+1000000*i, skills[23], 1.5))
		for i in range(1): tasks[1487].manpowers.append(Manpower(163710+1000000*i, skills[23], 0.5))
		for i in range(1): tasks[1488].manpowers.append(Manpower(163836+1000000*i, skills[6], 0))
		for i in range(1): tasks[1488].manpowers.append(Manpower(163835+1000000*i, skills[8], 0))
		for i in range(2): tasks[1493].manpowers.append(Manpower(164028+1000000*i, skills[8], 40))
		for i in range(2): tasks[1495].manpowers.append(Manpower(163829+1000000*i, skills[1], 0.1))
		for i in range(1): tasks[1502].manpowers.append(Manpower(163804+1000000*i, skills[6], 4.5))
		for i in range(1): tasks[1543].manpowers.append(Manpower(163801+1000000*i, skills[7], 10))
		for i in range(1): tasks[1543].manpowers.append(Manpower(163800+1000000*i, skills[6], 10))
		for i in range(1): tasks[1544].manpowers.append(Manpower(163803+1000000*i, skills[6], 1))
		for i in range(2): tasks[1545].manpowers.append(Manpower(163808+1000000*i, skills[6], 6))
		for i in range(6): tasks[1557].manpowers.append(Manpower(163818+1000000*i, skills[6], 8))
		for i in range(3): tasks[1558].manpowers.append(Manpower(163821+1000000*i, skills[6], 1))
		for i in range(1): tasks[1567].manpowers.append(Manpower(164023+1000000*i, skills[8], 8))
		for i in range(1): tasks[1570].manpowers.append(Manpower(164191+1000000*i, skills[8], 15))
		for i in range(2): tasks[1571].manpowers.append(Manpower(164096+1000000*i, skills[8], 40))
		for i in range(1): tasks[1571].manpowers.append(Manpower(163353+1000000*i, skills[10], 8))
		for i in range(1): tasks[1615].manpowers.append(Manpower(163344+1000000*i, skills[8], 10))
		for i in range(1): tasks[1616].manpowers.append(Manpower(163847+1000000*i, skills[6], 335.9))
		for i in range(1): tasks[1616].manpowers.append(Manpower(163346+1000000*i, skills[11], 92))
		for i in range(1): tasks[1616].manpowers.append(Manpower(163345+1000000*i, skills[8], 240))
		for i in range(1): tasks[1616].manpowers.append(Manpower(163834+1000000*i, skills[4], 20))
		for i in range(1): tasks[1616].manpowers.append(Manpower(163846+1000000*i, skills[10], 10))
		for i in range(1): tasks[1617].manpowers.append(Manpower(163995+1000000*i, skills[8], 30))
		for i in range(2): tasks[1635].manpowers.append(Manpower(163745+1000000*i, skills[1], 1.5))
		for i in range(1): tasks[1635].manpowers.append(Manpower(163743+1000000*i, skills[4], 2))
		for i in range(1): tasks[1635].manpowers.append(Manpower(163742+1000000*i, skills[5], 1))
		for i in range(3): tasks[1635].manpowers.append(Manpower(163762+1000000*i, skills[6], 2))
		for i in range(2): tasks[1636].manpowers.append(Manpower(163752+1000000*i, skills[1], 1.5))
		for i in range(2): tasks[1636].manpowers.append(Manpower(163750+1000000*i, skills[23], 2))
		for i in range(4): tasks[1636].manpowers.append(Manpower(163759+1000000*i, skills[22], 2))
		for i in range(2): tasks[1636].manpowers.append(Manpower(163755+1000000*i, skills[4], 3))
		for i in range(3): tasks[1636].manpowers.append(Manpower(163761+1000000*i, skills[5], 1.5))
		for i in range(2): tasks[1636].manpowers.append(Manpower(163774+1000000*i, skills[6], 4.5))
		for i in range(3): tasks[1637].manpowers.append(Manpower(163784+1000000*i, skills[6], 4))
		for i in range(1): tasks[1637].manpowers.append(Manpower(163765+1000000*i, skills[7], 2))
		for i in range(9): tasks[1637].manpowers.append(Manpower(163788+1000000*i, skills[22], 5))
		for i in range(2): tasks[1638].manpowers.append(Manpower(163791+1000000*i, skills[5], 0.5))
		for i in range(3): tasks[1638].manpowers.append(Manpower(163770+1000000*i, skills[1], 8.6))
		for i in range(4): tasks[1638].manpowers.append(Manpower(163789+1000000*i, skills[4], 1))
		for i in range(1): tasks[1641].manpowers.append(Manpower(163405+1000000*i, skills[4], 0.8))
		for i in range(2): tasks[1642].manpowers.append(Manpower(163379+1000000*i, skills[5], 1))
		for i in range(2): tasks[1643].manpowers.append(Manpower(164195+1000000*i, skills[8], 15))
		for i in range(2): tasks[1644].manpowers.append(Manpower(164199+1000000*i, skills[8], 15))
		for i in range(2): tasks[1646].manpowers.append(Manpower(164207+1000000*i, skills[8], 15))
		for i in range(3): tasks[1666].manpowers.append(Manpower(163812+1000000*i, skills[6], 5))
		for i in range(3): tasks[1694].manpowers.append(Manpower(164254+1000000*i, skills[27], 80))
		for i in range(2): tasks[1694].manpowers.append(Manpower(164226+1000000*i, skills[5], 40))
		for i in range(2): tasks[1694].manpowers.append(Manpower(164245+1000000*i, skills[28], 6))
		for i in range(5): tasks[1694].manpowers.append(Manpower(164278+1000000*i, skills[29], 14))
		for i in range(1): tasks[1694].manpowers.append(Manpower(163854+1000000*i, skills[25], 40))
		for i in range(1): tasks[1694].manpowers.append(Manpower(163853+1000000*i, skills[14], 110))
		for i in range(1): tasks[1694].manpowers.append(Manpower(163900+1000000*i, skills[22], 6))
		for i in range(3): tasks[1694].manpowers.append(Manpower(164229+1000000*i, skills[26], 100))
		for i in range(1): tasks[1714].manpowers.append(Manpower(163511+1000000*i, skills[5], 0.1))
		for i in range(2): tasks[1778].manpowers.append(Manpower(163697+1000000*i, skills[7], 3))
		for i in range(5): tasks[2053].manpowers.append(Manpower(164089+1000000*i, skills[12], 350))
		for i in range(1): tasks[2053].manpowers.append(Manpower(164090+1000000*i, skills[21], 8))
		for i in range(1): tasks[5008].manpowers.append(Manpower(163460+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[5009].manpowers.append(Manpower(163470+1000000*i, skills[5], 0.1))
		for i in range(1): tasks[5216].manpowers.append(Manpower(163933+1000000*i, skills[4], 0.5))
		for i in range(1): tasks[5217].manpowers.append(Manpower(163934+1000000*i, skills[5], 0.2))
		for i in range(1): tasks[5218].manpowers.append(Manpower(163935+1000000*i, skills[22], 0.5))
		for i in range(2): tasks[5704].manpowers.append(Manpower(163632+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[5705].manpowers.append(Manpower(163669+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[5709].manpowers.append(Manpower(163639+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[5734].manpowers.append(Manpower(163065+1000000*i, skills[6], 1))
		for i in range(2): tasks[5736].manpowers.append(Manpower(163206+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[5738].manpowers.append(Manpower(163254+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[5739].manpowers.append(Manpower(163123+1000000*i, skills[6], 1.3))
		for i in range(1): tasks[5740].manpowers.append(Manpower(163132+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[5750].manpowers.append(Manpower(164138+1000000*i, skills[8], 24))
		for i in range(2): tasks[5753].manpowers.append(Manpower(163208+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[5755].manpowers.append(Manpower(162917+1000000*i, skills[6], 1))
		for i in range(4): tasks[5761].manpowers.append(Manpower(163311+1000000*i, skills[6], 0.5))
		for i in range(1): tasks[5765].manpowers.append(Manpower(163725+1000000*i, skills[9], 40))
		for i in range(1): tasks[5765].manpowers.append(Manpower(163350+1000000*i, skills[10], 30))
		for i in range(1): tasks[5765].manpowers.append(Manpower(163349+1000000*i, skills[8], 100))
		for i in range(1): tasks[5765].manpowers.append(Manpower(163726+1000000*i, skills[6], 38))
		for i in range(1): tasks[5765].manpowers.append(Manpower(163839+1000000*i, skills[11], 1))
		for i in range(2): tasks[5769].manpowers.append(Manpower(163634+1000000*i, skills[6], 0.2))
		for i in range(1): tasks[5771].manpowers.append(Manpower(163824+1000000*i, skills[8], 40))
		for i in range(1): tasks[5771].manpowers.append(Manpower(163826+1000000*i, skills[10], 4))
		for i in range(1): tasks[5771].manpowers.append(Manpower(163825+1000000*i, skills[11], 4))
		for i in range(1): tasks[5790].manpowers.append(Manpower(163724+1000000*i, skills[4], 0.6))
		for i in range(1): tasks[5790].manpowers.append(Manpower(163723+1000000*i, skills[6], 0.6))
		for i in range(2): tasks[5791].manpowers.append(Manpower(163662+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[5792].manpowers.append(Manpower(163635+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[5793].manpowers.append(Manpower(163637+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[5794].manpowers.append(Manpower(163660+1000000*i, skills[6], 0.3))
		for i in range(2): tasks[5795].manpowers.append(Manpower(163657+1000000*i, skills[6], 0.5))
		for i in range(2): tasks[5826].manpowers.append(Manpower(164205+1000000*i, skills[8], 15))
		for i in range(1): tasks[5827].manpowers.append(Manpower(163354+1000000*i, skills[8], 40))
		for i in range(1): tasks[5827].manpowers.append(Manpower(163356+1000000*i, skills[10], 10))
		for i in range(1): tasks[5827].manpowers.append(Manpower(163355+1000000*i, skills[11], 40))
		for i in range(2): tasks[5828].manpowers.append(Manpower(163943+1000000*i, skills[6], 11))
		for i in range(3): tasks[5829].manpowers.append(Manpower(164040+1000000*i, skills[6], 360))
		for i in range(2): tasks[5850].manpowers.append(Manpower(163661+1000000*i, skills[6], 0.2))
		for i in range(2): tasks[7266].manpowers.append(Manpower(164215+1000000*i, skills[8], 100))
		for i in range(2): tasks[7286].manpowers.append(Manpower(164249+1000000*i, skills[8], 20))
		for i in range(4): tasks[13047].manpowers.append(Manpower(163951+1000000*i, skills[8], 0))
		for i in range(1): tasks[13047].manpowers.append(Manpower(163952+1000000*i, skills[10], 0))
		for i in range(1): tasks[13047].manpowers.append(Manpower(163953+1000000*i, skills[11], 0))
		for i in range(1): tasks[13047].manpowers.append(Manpower(163967+1000000*i, skills[16], 0))
		for i in range(1): tasks[13050].manpowers.append(Manpower(163973+1000000*i, skills[11], 0))
		for i in range(1): tasks[13050].manpowers.append(Manpower(163974+1000000*i, skills[16], 0))
		for i in range(4): tasks[13050].manpowers.append(Manpower(163971+1000000*i, skills[8], 0))
		for i in range(1): tasks[13050].manpowers.append(Manpower(163972+1000000*i, skills[10], 0))
		for i in range(2): tasks[16808].manpowers.append(Manpower(164286+1000000*i, skills[8], 5))
		for i in range(4): tasks[16898].manpowers.append(Manpower(164292+1000000*i, skills[8], 4))
		for i in range(1): tasks[16898].manpowers.append(Manpower(163954+1000000*i, skills[10], 2))
		for i in range(1): tasks[16898].manpowers.append(Manpower(163955+1000000*i, skills[11], 2))
		for i in range(1): tasks[16899].manpowers.append(Manpower(163975+1000000*i, skills[8], 5))
		for i in range(1): tasks[16899].manpowers.append(Manpower(163976+1000000*i, skills[10], 5))
		for i in range(1): tasks[16899].manpowers.append(Manpower(163977+1000000*i, skills[11], 5))
		for i in range(4): tasks[16988].manpowers.append(Manpower(164295+1000000*i, skills[8], 4))
		for i in range(1): tasks[16988].manpowers.append(Manpower(163956+1000000*i, skills[10], 2))
		for i in range(1): tasks[16988].manpowers.append(Manpower(163957+1000000*i, skills[11], 2))
		for i in range(1): tasks[18281].manpowers.append(Manpower(164078+1000000*i, skills[8], 4))
		for i in range(1): tasks[20388].manpowers.append(Manpower(163698+1000000*i, skills[14], 8))
		for i in range(1): tasks[20389].manpowers.append(Manpower(164042+1000000*i, skills[14], 4))
		for i in range(2): tasks[20390].manpowers.append(Manpower(164273+1000000*i, skills[14], 16))
		for i in range(1): tasks[20391].manpowers.append(Manpower(163845+1000000*i, skills[14], 8))
		for i in range(3): tasks[20393].manpowers.append(Manpower(163799+1000000*i, skills[7], 3))
		for i in range(1): tasks[20402].manpowers.append(Manpower(163964+1000000*i, skills[7], 0.2))
		for i in range(1): tasks[20403].manpowers.append(Manpower(163965+1000000*i, skills[22], 1.5))
		for i in range(1): tasks[20404].manpowers.append(Manpower(163966+1000000*i, skills[6], 1.3))

		for task in tasks.values():
			task.precal()

		self.assets = assets.values()
		self.tasks = tasks.values()		
		self.schedule = schedule