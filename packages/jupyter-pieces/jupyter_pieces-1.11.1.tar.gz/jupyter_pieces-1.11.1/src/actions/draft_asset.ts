import ConnectorSingleton from '../connection/connector_singleton';
import {
  AssetsDraftRequest,
  ClassificationSpecificEnum,
} from '@pieces.app/client';
import { SeedTypeEnum } from '@pieces.app/client';

export const draft_asset = ({ text }: { text: string }) => {
  const config = ConnectorSingleton.getInstance();
  const params: AssetsDraftRequest = {
    seed: {
      asset: {
        application: config.context.application,
        format: {
          fragment: {
            string: {
              raw: text,
            },
          },
          classification: {
            specific: ClassificationSpecificEnum.Py,
          },
        },
      },
      type: SeedTypeEnum.Asset,
    },
  };
  return config.assetsApi.assetsDraft(params);
};
