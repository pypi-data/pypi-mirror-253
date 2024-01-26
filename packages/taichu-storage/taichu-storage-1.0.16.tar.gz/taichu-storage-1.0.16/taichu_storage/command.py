import argparse
import logging
import os
import sys
from taichu_storage.obs_client import StorageObs

logging.basicConfig(level=logging.INFO,  # 打印日志等级
                    format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(threadName)s : %(message)s',  # 日志内容
                    datefmt='[%Y-%m-%d %H:%M:%S]',  # 日期格式
                    # filename='./my.log',  # 日志存放位置
                    # filemode='w'
                    )
# 实例化一个logger
logger = logging.getLogger(__name__)


def cli():
    parser = argparse.ArgumentParser(description="""Taichu Storage Tools""")
    parser.add_argument('action', action="store", choices=['cp'])
    parser.add_argument('source', action="store", type=str)
    parser.add_argument('destination', action="store", type=str)
    parser.add_argument('--ak', required=False, action="store",
                        help="""Specify the access key""")
    parser.add_argument('--sk', required=False, action="store", type=str,
                        help="""Specify the secret key""")
    parser.add_argument('--endpoint', required=False, action="store", type=str,
                        help="""Specify the endpoint""")
    parser.add_argument('--retry_times', required=False, default=3, action="store", type=int,
                        help="""Specify the retry times""")

    args = parser.parse_args()

    if args.source is None or args.destination is None:
        logger.info("Please specify both source and destination")
        sys.exit(1)
    retry_times = args.retry_times
    if retry_times and retry_times <= 0:
        retry_times = 100000

    logger.info("Copying {} to {}".format(args.source, args.destination))
    if args.source.startswith("obs://") and not args.destination.startswith("obs://"):
        download_from_obs(args.source, args.destination, ak=args.ak, sk=args.sk, endpoint_url=args.endpoint,
                          retry_times=retry_times)
    elif not args.source.startswith("obs://") and args.destination.startswith("obs://"):
        upload_to_obs(args.source, args.destination, ak=args.ak, sk=args.sk, endpoint_url=args.endpoint)
    else:
        logger.info("Not supported yet")


def download_from_obs(src, dest, ak=None, sk=None, endpoint_url=None,
                      retry_times=None):
    src_bucket, src_key = parse_obs_path(src)
    client = StorageObs(cfgs={
        'bucket': src_bucket,
        'ak': ak,
        'sk': sk,
        'endpoint_url': endpoint_url})
    if src_key.endswith("/"):
        client.download_dir(src_key, dest, retry_times=retry_times)
    else:
        client.download_file(src_key, dest, retry_times=retry_times)


def upload_to_obs(src, dest, ak=None, sk=None, endpoint_url=None):
    dest_bucket, dest_key = parse_obs_path(dest)

    if not os.path.exists(src):
        raise Exception("src path {} does not exist".format(src))

    client = StorageObs(cfgs={
        'bucket': dest_bucket,
        'ak': ak,
        'sk': sk,
        'endpoint_url': endpoint_url})

    if os.path.isfile(src):
        client.upload_file(src, dest_key)
        return

    client.upload_dir(src, dest_key)


def parse_obs_path(obs_path):
    if obs_path.startswith("obs://"):
        obs_path = obs_path[6:]

    bucket = obs_path.split("/")[0]
    key = obs_path[len(bucket) + 1:]

    return bucket, key


if __name__ == '__main__':
    cli()
