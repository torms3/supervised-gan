from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--display_freq', type=int, default=100, help='frequency of showing training results on screen')
        self.parser.add_argument('--print_freq', type=int, default=100, help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int, default=5000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=5, help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        self.parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=100, help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--no_lsgan', action='store_true', help='do *not* use least square GAN, if false, use vanilla GAN')
        # self.parser.add_argument('--lambda_A', type=float, default=10.0, help='weight for cycle loss (A -> B -> A)')
        # self.parser.add_argument('--lambda_B', type=float, default=10.0, help='weight for cycle loss (B -> A -> B)')
        self.parser.add_argument('--lambda_A', type=float, default=10.0, help='weight for regression loss (A -> B)')
        self.parser.add_argument('--lambda_B', type=float, default=10.0, help='weight for regression loss (B -> A)')
        self.parser.add_argument('--n_update_G', type=int, default=1, help='# of updates of G')
        self.parser.add_argument('--n_update_D', type=int, default=1, help='# of updates of D')
        self.parser.add_argument('--lambda_D', type=float, default=[1.0], nargs='+', help='weight for discriminators')
        self.parser.add_argument('--pool_size', type=int, default=50, help='the size of image buffer that stores previously generated images')
        self.parser.add_argument('--no_html', action='store_true', help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.add_argument('--no_cgan', action='store_true', help='do *not* use cGAN (, use GAN)')
        self.parser.add_argument('--noise_pool_size', type=int, default=100, help='the size of buffer for fixed noise to sample from')
        self.parser.add_argument('--optimizer', type=str, default='adam', help='which optimizer to use?')
        self.parser.add_argument('--clamp_lower', type=float, default=-0.01)
        self.parser.add_argument('--clamp_upper', type=float, default=0.01)
        self.parser.add_argument('--train_D_on_fake_fake_pair', action='store_true', help='')
        self.parser.add_argument('--train_G_on_fake_fake_pair', action='store_true', help='')
        self.parser.add_argument('--pool_reject_prob', type=float, default=0.5, help='probability of reject a new sample when query')
        self.parser.add_argument('--really_CausalGAN', action='store_true', help='if true, G will maximize NLL of Anti-Labeler')
        self.parser.add_argument('--lambda_fake_cycle', type=float, default=1.0, help='fake cycle')
        self.parser.add_argument('--which_model_to_load', nargs='+', default=[''], help='which pretrained model(s) to load?')
        self.parser.add_argument('--which_model_to_load_label', nargs='+', default=[''], help='which pretrained model(s) to load?')
        self.parser.add_argument('--no_logD_trick', action='store_true', help='do *not* use log(D) trick training GAN')

        # for two-stage model only:
        self.parser.add_argument('--lr1', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--lr2', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--lambda_D1', type=float, default=[1.0], nargs='+', help='weight for discriminators')
        self.parser.add_argument('--no_lsgan1', action='store_true', help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.add_argument('--n_update_D1', type=int, default=1, help='# of updates of D1')
        self.parser.add_argument('--lambda_D2', type=float, default=[1.0], nargs='+', help='weight for discriminators')
        self.parser.add_argument('--no_lsgan2', action='store_true', help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.add_argument('--n_update_D2', type=int, default=1, help='# of updates of D2')
        self.parser.add_argument('--sequential_train', action='store_true', help='use sequential training')
        self.parser.add_argument('--which_epoch_sequential', type=str, default='seq', help='which epoch to load for sequential training?')
        self.parser.add_argument('--use_multi_class_GAN', action='store_true', help='use 3-way classification in D2')
        self.parser.add_argument('--detach_G1_from_G2_x', action='store_true', help='do *not* update G1 when updating G2')
        self.parser.add_argument('--detach_G1_from_G2_y', action='store_true', help='do *not* update G1 when updating G2')
        self.parser.add_argument('--GAN_losses_D2', nargs='+', default=['real_fake'], help='what (A, B) pairs are included in binary GAN loss for D2?')
        self.parser.add_argument('--GAN_losses_G2', nargs='+', default=['real_fake'], help='what (A, B) pairs are included in binary GAN loss for G2?')
        self.parser.add_argument('--use_random_crop_G2', action='store_true', help='random crop inputs for G2 and D2')
        self.parser.add_argument('--random_crop_size', type=int, default=512, help='size of random crop')
        self.parser.add_argument('--lambda_A_cycle', type=float, default=10.0, help='weight for cycle loss (A -> B -> A)')
        self.parser.add_argument('--lambda_B_cycle', type=float, default=10.0, help='weight for cycle loss (B -> A -> B)')
        self.parser.add_argument('--use_fixed_noise1', action='store_true', help='noise1 sampled from fixed pool')
        self.parser.add_argument('--lambda_G1', type=float, default=1, help='weight for G1')
        self.parser.add_argument('--lambda_G2', type=float, default=1, help='weight for G2')

        self.isTrain = True